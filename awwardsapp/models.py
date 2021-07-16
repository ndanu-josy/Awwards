from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    profile_picture = CloudinaryField('pic')
    bio = models.CharField(max_length=50)  
    projects = models.CharField(max_length=50)  
    contact_info = models.CharField(max_length=60,blank=True)
   
class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = CloudinaryField('img')
    description = models.CharField(max_length=400)
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    