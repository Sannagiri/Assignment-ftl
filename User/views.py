from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.

def loginpage(request):

    """
    -- It is post method 
    -- Accepts username and password from login.html as input arguments
    -- Then authenticates with database for given username and password
    -- If username and password are available and correct then it displays the home page
    -- If there is no correct match then error message is displayed

    """

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('User:detailviewpage')
        else: 
            messages.info(request,'Username or Password is incorrect')

    context={
        
    }
    return render(request,'user/login.html',context)

def logoutpage(request):

    """
    -- It is logout functionality of django and redirects to login page

    """

    logout(request)
    return redirect('User:loginpage')

"""
-- API endpoint that allows to view the User details and respective activity periods
-- UserSerializer inherits the ActivitySerializer for combining the data from two models
-- from different menthods here we are displaying using GET method
"""

@api_view(['GET'])
def userdetailview(request):

    members=User.objects.all()
    user_serializer=UserSerializer(members,many=True)
    print(user_serializer.data)
    return Response({
        'ok':True,
        'members':user_serializer.data
    })
