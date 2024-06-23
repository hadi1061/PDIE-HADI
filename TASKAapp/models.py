from django.db import models

# Create your models here.
class PARENTS(models.Model):
    ICNUM = models.CharField(max_length=255,primary_key=True)
    NAME = models.TextField(max_length=225)
    USERNAME=models.TextField(max_length=255)
    PASSWORD=models.CharField(max_length=225)
    EMAIL= models.EmailField()
    ADDRESS=models.CharField(max_length=225)
    NOMPHONE = models.CharField(max_length=255)
    RELATIONSHIP=models.TextField(max_length=255)
    RELIGION=models.TextField(max_length=225)
    INCOME=models.IntegerField()

class Admin(models.Model):
    username=models.CharField(max_length=225,primary_key=True)
    PASSWORD=models.CharField(max_length=225)
    NAME=models.CharField(max_length=225)
    
class STAFF(models.Model):
    STICNUM=models.CharField(max_length=225,primary_key=True)
    NAME=models.TextField(max_length=225)
    PASSWORD=models.CharField(max_length=225)
    EMAIL=models.EmailField()
    PHONENUMBER=models.CharField(max_length=225)
    ADDRESS=models.CharField(max_length=225)
    POSSITION=models.TextField(max_length=225)
    EDUCATION=models.CharField(max_length=225)
    username = models.ForeignKey(Admin, on_delete=models.CASCADE)

class CHILD(models.Model):
    mykadnum=models.CharField(max_length=125,primary_key=True)
    ICNUM = models.ForeignKey(PARENTS, on_delete=models.CASCADE)
    username = models.ForeignKey(Admin, on_delete=models.CASCADE)
    STICNUM= models.ForeignKey(STAFF, on_delete=models.CASCADE)
    cname=models.TextField(max_length=125)
    age=models.CharField(max_length=125)
    salinanmykid=models.ImageField(upload_to='images/')
    salinanICparent=models.ImageField(upload_to='images/')
    salinansuratberanak=models.ImageField(upload_to='images/')
    salinanimunisasianak=models.ImageField(upload_to='images/')
    interfacebukukesihatan=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"{self.cname} ({self.mykadnum})"