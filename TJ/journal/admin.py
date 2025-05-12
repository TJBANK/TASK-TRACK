from django.contrib import admin

# Register your models here.

#here we import our thought model in the model.py file into our admin.py file
from .models import Thought, Profile

#here we register our thought model inside our admin page
admin.site.register(Thought)

#setting up a functionality for file handling 
admin.site.register(Profile)
