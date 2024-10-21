from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your models here.
class register(request):
    name=request.POST['name']
    email=request.POST['email']
    phone_number=request.POST['phone_number']
    account=request.POST['account']
    message=request.POST['message']


    user=User.objects.create_user(name=name)
    print("we wil call back you")
   
 

   