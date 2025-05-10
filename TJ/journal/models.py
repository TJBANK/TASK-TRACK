from django.db import models

from django.contrib.auth.models import User

class Thought(models.Model):
    
    title = models.CharField(max_length=150)
    content = models.CharField(max_length= 500)
    
    date_posted = models.DateTimeField(auto_now_add= True)
    
    #this command will helps us delete the data of a user if the user doesn't exist anymore 
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
