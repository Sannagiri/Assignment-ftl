from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
    # Start page for app
    path('',views.loginpage,name='loginpage'),

    # Logout implementation application
    path('logout/',views.logoutpage,name='logoutpage'),

    # Displays the details of all users with activity periods in json format -- API Endpoint
    path('userdetailview-api/',views.userdetailview,name='detailviewpage'),
    
]