from django.shortcuts import render, redirect

# importing our custom created forms'create_user_form' and 'Update_User_form' from forms.py file
from .forms import create_user_form, LoginForm, ThoughtForm, Update_User_Form, UpdateProfileForm 

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate, login, logout

# here we import this library to protect our views- preventing anyone from casually entering into the website without logging in any credentials
from django.contrib.auth.decorators import login_required

#importing the default django flash messages 
from django.contrib import messages

from . models import Thought, Profile

from django.contrib.auth.models import User



# Create your views or our functions here.

def homepage(request):
    
    return render(request, 'journal/index.html')




def register(request):
    
    form = create_user_form()
    
    if request.method == 'POST':
        
        #this will take all the data that has been entered by the user and store it including username, email etc
        form = create_user_form(request.POST)
        
        # verify if the form the user filled matches with what is expected 
        if form.is_valid():
            
            #after a user creates an account,wait before u save the data
            current_user = form.save(commit=False)
            
            #after saving...
            form.save()
            
            #we tell django to create a profile object and bind it to the user who just created the account.
            profile = Profile.objects.create(user=current_user)
            
            
            
            
            
            #setting up our flash messages..
            messages.success(request, "User created!")
            
            # direct him to the login-page-path after registration
            return redirect('login_page')
            
    #here we output the form that we have created onto our template
    
    context = {'RegistrationForm': form}
    
    return render(request, 'journal/register.html', context)
    





def login(request):
    
    form = LoginForm()
    
    if request.method =='POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # here checking if the user has the correct details.. and if it matches in our database 
            user = authenticate(request, username=username, password=password)
            
            # here if the user exists in our database.. the following comannd will allow him to the dashboard
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('dash_board')
    
    context ={'LoginForm': form}       
    
    return render(request, 'journal/login.html', context)
  
  
  
  
def logout(request):
    
    auth.logout(request)
    
    return redirect("") 
  
  
 
# below command will force users to login before accessing the dashbaord page !!
@login_required(login_url='login_page')
def dashboard(request):
    
    #checking if the user in the database is matching the current user logged in..
    profile_pic = Profile.objects.get(user=request.user)
    
    context ={'PROFILE_IMAGE':profile_pic}
    
    return render(request, 'journal/dashboard.html', context)
  

@login_required(login_url='login_page')
def  createthought(request):
    
    form = ThoughtForm()
    
    if request.method == "POST":
        
        form = ThoughtForm(request.POST)
        
        if form.is_valid():
            
            #here we inform django to send the information entered by any-user into our 
            # database but wait a little while cos we wanna add something in terms of the foreign key
            thought = form.save(commit=False)
            
            #this will help us assign the data content entered by a user to their coreesponding account details so it doesn't mix
            thought.user = request.user
            
        
            thought.save()
            
            return redirect("dash_board")
        
            
    context = {'CreateThoughtForm': form}
    
    #this will link our html template to our views & urls files
    return render(request, 'journal/create-thought.html', context)


@login_required(login_url='login_page')
def viewthought(request):
    
    #getting the id of the current logged-in user
    current_user = request.user.id
    
    #retrieving all the thoughts a user has created with their account
    thought = Thought.objects.all().filter(user= current_user)
    
    
    context = {'mythoughts': thought}
    
    
    
    return render(request,  'journal/my-thought.html', context)


@login_required(login_url='login_page')
def updatethought(request, pk):
    
    #the try/except command will disable users form altering the data content of another user,
    # and then be redirected to the to the users my thought page
    try:
        
        thought = Thought.objects.get(id=pk, user= request.user)
    
    
    except:
        
        return redirect('my_thoughts')
    
    #retrieving the current content of the data created by the user
    form = ThoughtForm(instance=thought)
    
    if request.method == 'POST':
        
        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid():
            
            form .save()

            return redirect('my_thoughts')
        
    
    context = {'UpdateThought': form}
    
    return render(request,  'journal/update-thought.html', context)




@login_required(login_url='login_page')
def deletethought(request, pk):
    
    #this can also be describe as an error handling mechanism for our users
    try:
        
        thought = Thought.objects.get(id=pk, user= request.user)
    
    
    except:
        
        return redirect('my_thoughts')
    
    if request.method == 'POST':
        
        thought.delete()
        
        return redirect('my_thoughts')
    
    return render(request,  'journal/delete-thought.html')


@login_required(login_url='login_page')
def ProfileManagement(request):
    
    # getting the current data of the user logged-in in our website
    form = Update_User_Form(instance=request.user)
    
    #gettiing the current profile photo the user is using which is likely to be the defualt photo if the user is new
    profile = Profile.objects.get(user=request.user)
    
    #getting the latest data on the user logged in...
    form_2 = UpdateProfileForm(instance=User)
    
    
    
    # this commnd simple means a user wants to send someting. eg-a form
    if request.method == 'POST':
        
        #updating the form after the system see its a post request from the user
        form = Update_User_Form(request.POST, instance= request.user)
        
        
        #we want the user to send a post request, where they will be able to upload a file based on the particlar instance the user that is currently logges in to overwrite the default photo.... 
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        
        
        
        
        #a chehck before the user can udpate his/her form ..
        if form.is_valid():
            
            form.save()
            
            return redirect('dash_board')
        
        
        
        #a chehck before a user can changed the profile.
        if form_2.is_valid():
            
            form_2.save()
            
            return redirect('dash_board')
        
        
        
    
    context = {'UserupdateForm': form, 'ProfileUpdateForm': form_2}
    
    return render(request,  'journal/profile-manage.html', context)

    
@login_required(login_url='login_page')
def deleteaccount(request):
      
       # this commnd simple means a user wants to send someting. eg-a form
    if request.method == 'POST':
        
        #performing a query data to get access to whoever is currently issuing that task 
        deleteUser = User.objects.get(username=request.user)
        
        deleteUser = delete()
        
        return redirect('register')
        
    
    return render(request, 'journal/delete-account.html')

