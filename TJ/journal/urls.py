
from django.contrib import admin
from django.urls import path

# we import our views from the views.py file
from .import views 

#importing django in-built views for our password reset
from django.contrib.auth import views as auth_views

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
    
    
    
    #PASSWORD-MANAGEMENT
    
    # 1  - a URL to allow us to enter our email in order to receive a passowrd reset
    path('reset_password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    
    
    # 2 - a URL showing us a success message stating that an email was sent to reset our password
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    
    # 3 - a URL to send a link to our email, so that we can reset our password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= "password_reset_confirm"),
    
    # 4 a URL to show a success that our password was changed
    
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
]