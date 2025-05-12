
# importing the default django userCreationForm 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# importing the default django usermodel
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

#here we import the base model-form-class which we allow us to access the base class for creating a model form
from django.forms import ModelForm

#importing the model we wanna work on
from. models import Thought, Profile




class ThoughtForm(ModelForm):
    
    class Meta:
        
        model = Thought
        fields = ['title', 'content',]
        
       

class create_user_form(UserCreationForm):
    
    #specify our fields
    class Meta:
        model= User
        fields = ['username','email', 'password1', 'password2']
        



class LoginForm(AuthenticationForm):
    
    # specifying our fields
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
    
    
    
    
class Update_User_Form(forms.ModelForm):
    
    #this is an inbuilt django funtionality we can always use 
    password = None
    
    #specify our fields
    class Meta:
        model= User
        
        fields = ['username','email',]
        exclude = ['password1', 'password2',]
        
        
#this model class will allow us to upload a profile-pic
class UpdateProfileForm(forms.ModelForm):
    
    #
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        
        model = Profile
        fields = ['profile_pic',]
        
        
        
    