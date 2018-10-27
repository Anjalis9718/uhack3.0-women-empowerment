from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    Area_of_Interests = models.CharField(max_length=1000,blank=True)
    Extra_Skills = models.CharField(max_length=10000,blank=True)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Counsellor(models.Model):
    NAME = models.CharField(max_length=100)
    DEALS_REGARDING = models.CharField(max_length=200)
    CONTACT_NO = models.CharField(max_length=12)
    EMAIL = models.EmailField(max_length=70)

    def __str__(self):
        return self.NAME

class n_g_o (models.Model):
    NAME = models.CharField(max_length=200)
    ADDRESS = models.CharField(max_length=200)
    WEBPAGE = models.URLField()
    CONTACT_NO =models.CharField(max_length=12)
    EMAIL = models.EmailField(max_length=70)

    def __str__(self):
        return self.NAME

class rate_organisation(models.Model):
    
    Username = models.CharField(max_length=1000)
    Organization_name=models.CharField(max_length=1000)
    Problem_faced=models.CharField(max_length=10000)
    Suggestion=models.CharField(max_length=10000)

    def __str__(self):
        return self.Organization_name
