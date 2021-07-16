from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    profile_picture = CloudinaryField('pic')
    bio = models.CharField(max_length=50)  
    projects = models.CharField(max_length=50)  
    contact_info = models.CharField(max_length=60,blank=True)
   
    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Project(models.Model):
    title = models.CharField(max_length=60,blank=True)
    image = CloudinaryField('img')
    description = models.CharField(max_length=400)
    link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def save_projects(self):
        self.user

    def delete_projects(self):
        self.delete()    

    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()

RATES = [
(1,'1'),
(2,'2'),
(3,'3'),
(4,'4'),
(5,'5'),
(6,'6'),
(7,'7'),
(8,'8'),
(9,'9'),
(10,'10'),
]
class Rating(models.Model):    
    design = models.PositiveSmallIntegerField(choices = RATES,default= 0)
    usability = models.PositiveSmallIntegerField(choices = RATES,default = 0)
    content = models.PositiveSmallIntegerField(choices = RATES,default = 0)
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()        