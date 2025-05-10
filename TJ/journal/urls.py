
from django.contrib import admin
from django.urls import path

# we import our views from the views.py file
from .import views 

urlpatterns = [
    
    path('', views.homepage, name=""),
    
    path('register/',views.register, name="register"),
    
    path('login_page/', views.login, name="login_page"),
    
    path('dash_board/', views.dashboard, name="dash_board"),
    
    path('log_out/', views.logout, name="log_out"),
    
    path('create_thought/', views.createthought, name="create_thought"),
    
    path('my_thoughts/', views. viewthought, name="my_thoughts"),
    
      #we add <str:pk> to make our url link dynamic
    path('update_thought/<str:pk>', views.updatethought, name="update_thought"),
     
      #we add <str:pk> to make our url link dynamic
    path('delete_thought/<str:pk>', views.deletethought, name="delete_thought"),
    
    path('profile_management/', views.ProfileManagement , name="profile_management"),
    
    path('delete_account/', views.deleteaccount, name="delete_account"),
    
    
]