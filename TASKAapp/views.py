from django.shortcuts import render
from .models import PARENTS,Admin,STAFF,CHILD
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
    return render(request,"home.html")

def selectlogin(request):
    return render(request,"selectlogin.html")

#parentregister____________________________________________________________________________________________
def parentregister(request):
    return render(request,"parentregister.html")

def funcparentregister(request):
    displaydata=PARENTS.objects.all().values()
    if request.method=='POST':
        ICNUM1=request.POST['ICNUM']
        NAME1=request.POST['NAME']
        USERNAME1=request.POST['USERNAME']   
        PASSWORD1=request.POST['PASSWORD']
        EMAIL1=request.POST['EMAIL']
        ADDRESS1=request.POST['ADDRESS']
        NOMPHONE1=request.POST['NOMPHONE']
        RELIGION1=request.POST['RELIGION']
        INCOME1=request.POST['INCOME']
        RELATIONSHIP1=request.POST['RELATIONSHIP']
        data = PARENTS(ICNUM=ICNUM1,NAME=NAME1,USERNAME=USERNAME1,PASSWORD=PASSWORD1,EMAIL=EMAIL1,ADDRESS=ADDRESS1,NOMPHONE=NOMPHONE1,RELIGION=RELIGION1,INCOME=INCOME1,RELATIONSHIP=RELATIONSHIP1)
        data.save()

        context={
            'displaydata' : displaydata,
            'message' : 'new user login'
         }
        
        return render(request,"parentregister.html",context)
    else:
        dict={
            'message':'',
            'displaydata' : displaydata,

        }
        return render (request,"parentregister.html",dict)
    
#parents login____________________________________________________________________________________________________________

def parentlogin(request):
    if (request.method == 'GET'):
        return render(request, 'parentlogin.html', {'message':' '})
    else:
        ICNUM = request.POST['ICNUM']
        PASSWORD = request.POST['PASSWORD']
        mycust = PARENTS.objects.all().filter(ICNUM=ICNUM,PASSWORD=PASSWORD)
        for x in mycust:
            if x.ICNUM==ICNUM and x.PASSWORD==PASSWORD:
                url = reverse('parenthome', kwargs={'ICNUM':ICNUM})
                return HttpResponseRedirect(url)
        return render(request, 'parentlogin.html', {'message':'Your password is incorrect.'})
    
def parenthome(request,ICNUM):
    myparent=PARENTS.objects.get(ICNUM=ICNUM)
    mychild = CHILD.objects.filter(ICNUM=ICNUM)
    dict = {
        'myparent':myparent,
        'mychild':mychild,
    }
    return render(request,'parenthome.html',dict)

#register child_____________________________________________________________________________________________________________________
def childregisterpage(request):
    return render(request,'registerchild.html')

#register using form 
from django.shortcuts import render, redirect
from .forms import childForm

def addchild(request):
    if request.method == 'POST':
        form = childForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('childregisterpage')  # Redirect to a success page or another appropriate page
    else:
        form = childForm()
    return render(request, 'registerchild.html', {'form': form})
 

#admin login ______________________________________________________________________________________________________________________


def adminlogin(request):
    if (request.method == 'GET'):
        return render(request, 'adminlogin.html', {'message':' '})
    else:
        username = request.POST['username']
        PASSWORD = request.POST['PASSWORD']
        mycust = Admin.objects.all().filter(username=username,PASSWORD=PASSWORD)
        for x in mycust:
            if x.username==username and x.PASSWORD==PASSWORD:
                url = reverse('adminhome', kwargs={'username':username})
                return HttpResponseRedirect(url)
        return render(request, 'adminlogin.html', {'message':'Your password is incorrect.'})
    
#admin home _______________________________________________________________________________________________________________________
def adminhome(request,username):
    myCHILD = CHILD.objects.all().values()
    myADMIN = Admin.objects.get(username=username)
    mystaff=STAFF.objects.all().values()
    dict={
        'myCHILD':myCHILD,
        'myADMIN':myADMIN,
        'mystaff':mystaff,
      }
    return render(request,'adminhome.html',dict)

#staff login________________________________________________________________________________________________________________________
def stafflogin(request):
    return render(request,'stafflogin.html')

def staffloginfunc(request):
    if (request.method == 'GET'):
        return render(request, 'stafflogin.html', {'message':' '})
    else:
        STICNUM = request.POST['STICNUM']
        PASSWORD = request.POST['PASSWORD']
        mycust = STAFF.objects.all().filter(STICNUM=STICNUM,PASSWORD=PASSWORD)
        for x in mycust:
            if x.STICNUM==STICNUM and x.PASSWORD==PASSWORD:
                url = reverse('staffhome', kwargs={'STICNUM':STICNUM})
                return HttpResponseRedirect(url)
        return render(request, 'stafflogin.html', {'message':'Your password is incorrect.'})
    
#stafffpage_____________________________________________________________________________________________________________________
def staffhome(request,STICNUM):
    mySTAFF = STAFF.objects.get(STICNUM=STICNUM)
    mychild = CHILD.objects.all().values()
    myparent = PARENTS.objects.all().values()
    
    dict={
        'mySTAFF':mySTAFF,
        'mychild':mychild,
        'myparent':myparent,
        
      }
    return render(request,'staffhome.html',dict)

#stafuserprofile________________________________________________________________________________________________________
def staffuserprofile(request,STICNUM):
    mySTAFF = STAFF.objects.get(STICNUM=STICNUM)

    dict={
        'mySTAFF':mySTAFF,
      }
    return render(request,'staffuserprofile.html',dict)


#staff edit profile_________________________________________________________________________________________________
def staffeditprofile(request, STICNUM):
    if request.method == "GET":
        mySTAFF = STAFF.objects.get(STICNUM=STICNUM)
        dict = {
            'mySTAFF':mySTAFF,
        }
        return render(request, 'staffeditprofile.html', dict)
    else:
        mySTAFF = STAFF.objects.get(STICNUM=STICNUM)
        NAME = request.POST['NAME']
        password = request.POST['PASSWORD']
        email = request.POST['EMAIL']
        phonenumber = request.POST['PHONENUMBER']
        address = request.POST['ADDRESS']
        possition = request.POST['POSSITION']
        education = request.POST['EDUCATION']
        if (NAME != ''):
            mySTAFF.NAME = NAME
        if (password != ''):
            mySTAFF.PASSWORD = password
        if (email != ''):
            mySTAFF.EMAIL = email
        if (phonenumber != ''):
            mySTAFF.PHONENUMBER = phonenumber
        if (address != ''):
            mySTAFF.ADDRESS= address
        if (possition != ''):
            mySTAFF.POSSITION = possition
        if (education != ''):
            mySTAFF.EDUCATION = education
        mySTAFF.save()
        url = reverse('staffeditprofile', kwargs={'STICNUM':STICNUM})
        return HttpResponseRedirect(url)
    

#childdetaill at staff_________________________________________________________________________________________________________
def childdetail(request,STICNUM,mykadnum):
    mySTAFF=STAFF.objects.get(STICNUM=STICNUM)
    myCHILD =CHILD.objects.get(mykadnum=mykadnum)
    dict = {
       'mySTAFF':mySTAFF,
       'myCHILD':myCHILD
    }
    return render(request, 'childdetail.html', dict)
#pluss staff__________________________________________________________________________________________________________________
def PLUSSTAFF(request):
    displaydata=STAFF.objects.all().values()
    if request.method=='POST':
        STICNUM1=request.POST['STICNUM']
        PASSWORD1=request.POST['PASSWORD']
        username=request.POST['username']
        fkusername = Admin.objects.get(username=username)
       
        data = STAFF(STICNUM=STICNUM1,PASSWORD=PASSWORD1,username=fkusername)
        data.save()
        context={
            'displaydata' : displaydata,
            'message' : 'new user login'
         }
        
        return render(request,"adminhome.html",context)
    else:
        dict={
            'message':'',
            'displaydata' : displaydata,

        }
        return render (request,"adminhome.html",dict)
    
#delete data child_________________________________________________________________________________________________________________
def deletedatachild(request, mykadnum):
    # Get the NutritionLog instance to be deleted, or return a 404 response if it doesn't exist
    data = get_object_or_404(CHILD,mykadnum=mykadnum)

    if request.method == 'POST':
        # If a POST request is received, delete the instance and redirect to a specific page
        data.delete()
        return render(request,'staffhome') 

#update staff at admin_______________________________________________________________________________________________________________________
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import STAFF, Admin

def staffupdate(request, username, STICNUM):
    if request.method == "GET":
        mySTAFF = get_object_or_404(STAFF, STICNUM=STICNUM)
        myADMIN = get_object_or_404(Admin, username=username)
        context = {
            'mySTAFF': mySTAFF,
            'myADMIN': myADMIN
        }
        return render(request, 'staffupdate.html', context)
    else:
        mySTAFF = get_object_or_404(STAFF, STICNUM=STICNUM)
        myADMIN = get_object_or_404(Admin, username=username)
        NAME = request.POST['NAME']
        password = request.POST['PASSWORD']
        email = request.POST['EMAIL']
        phonenumber = request.POST['PHONENUMBER']
        address = request.POST['ADDRESS']
        possition = request.POST['POSSITION']
        education = request.POST['EDUCATION']
        if NAME:
            mySTAFF.NAME = NAME
        if password:
            mySTAFF.PASSWORD = password
        if email:
            mySTAFF.EMAIL = email
        if phonenumber:
            mySTAFF.PHONENUMBER = phonenumber
        if address:
            mySTAFF.ADDRESS = address
        if possition:
            mySTAFF.POSSITION = possition
        if education:
            mySTAFF.EDUCATION = education
        mySTAFF.save()
        url = reverse('staffupdate', kwargs={'username': username, 'STICNUM': STICNUM})
        return HttpResponseRedirect(url)


#parents update child _____________________________________________________________________________________________
def updatechildparent(request, mykadnum,ICNUM):
    if request.method == "GET":
        myCHILD = CHILD.objects.get(mykadnum=mykadnum)
        myPARENTS = PARENTS.objects.get(ICNUM=ICNUM)
        dict = {
            'myCHILD':myCHILD,
            'myPARENTS':myPARENTS
        }
        return render(request, 'pareupdatechild.html', dict)
    else:
        myPARENTS = PARENTS.objects.get(ICNUM=ICNUM)
        myCHILD = CHILD.objects.get(mykadnum=mykadnum)
        cname = request.POST['cname']
        age = request.POST['age']
       
        if (cname != ""):
            myCHILD.cname = cname
        if (age != ""):
            myCHILD.age = age
      
        myCHILD.save()
        url = reverse('pareupdatechild', kwargs={'ICNUM':ICNUM , 'mykadnum':mykadnum})
        return HttpResponseRedirect(url)
    
#parents child detail_____________________________________________________________________________
def childdetailpare(request,ICNUM,mykadnum):
    myparent=PARENTS.objects.get(ICNUM=ICNUM)
    myCHILD =CHILD.objects.get(mykadnum=mykadnum)
    dict = {
       'myparent':myparent,
       'myCHILD':myCHILD
    }
    return render(request, 'parechilddetail.html', dict)