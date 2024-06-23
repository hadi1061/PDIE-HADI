from django.urls import path
from . import views 
from django.urls import path


urlpatterns = [
    path("",views.index , name = "home"),
    path("selectlogin",views.selectlogin , name = "selectlogin"),
    path("parentregister",views.parentregister , name = "parentregister"),
    path("funcparentregister",views.funcparentregister , name = "funcparentregister"),
    path("parentlogin",views.parentlogin , name = "parentlogin"),
    path("parenthome/<str:ICNUM>",views.parenthome,name="parenthome"),
    path("parenthome/pareupdatechild/<str:ICNUM>/<str:mykadnum>",views.updatechildparent,name="pareupdatechild"),
    path("adminlogin",views.adminlogin , name = "adminlogin"),
    path("adminhome/<str:username>",views.adminhome,name="adminhome"),
    path("adminhome/staffupdate/<str:username>/<str:STICNUM>", views.staffupdate, name="staffupdate"),
    path("stafflogin/",views.stafflogin,name="stafflogin"),
    path("staffloginfunc/",views.staffloginfunc,name="staffloginfunc"),
    path("staffhome/<str:STICNUM>",views.staffhome,name="staffhome"),
    path("staffhome/staffuserprofile/<str:STICNUM>/",views.staffuserprofile,name="staffuserprofile"),
    path("staffhome/staffuserprofile/staffeditprofile/<str:STICNUM>",views.staffeditprofile,name="staffeditprofile"), 
    path("PLUSSTAFF/",views.PLUSSTAFF,name="PLUSSTAFF"),
    path("childregisterpage/",views.childregisterpage,name="childregisterpage"),
    path("addchild/",views.addchild,name="addchild"),
    path("staffhome/detail/<str:STICNUM>/<str:mykadnum>",views.childdetail,name="detail"),
    path("parenthome/childdetailpare/<str:ICNUM>/<str:mykadnum>",views.childdetailpare,name="childdetailpare"),
    path('deletedatachild/<str:mykadnum>', views.deletedatachild, name='deletedatachild'),
]