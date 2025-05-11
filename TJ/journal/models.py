from django.db import models

from django.contrib.auth.models import User



#adding funtionality for admin to be able to create, update and delete a thought
class Thought(models.Model):
    
    title = models.CharField(max_length=150)
    content = models.CharField(max_length= 500)
    date_posted = models.DateTimeField(auto_now_add= True)
    
    #this command will helps us delete the data of a user if the user doesn't exist anymore 
    #and also link our user model to our profile model
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
    
    
    
#adding funtionality for admin to get profile picture
class Profile(models.Model):
    
    #Without null=True, the database will require a value for that field
    profile_pic = models.ImageField(null=True, blank=True, default='Default.png')
    
    #linking our user model to our profile model
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
    
    
