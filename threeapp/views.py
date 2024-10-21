from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.db import models
# threeapp/views.py

from .models import Registration



# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")

def ideagained(request):
    return render(request,"idea_gained.html")

def idea(request):
    return render(request,"idea.html")

def ouridea(request):
    return render(request,"our_idea.html")

def aboutpage(request):
    return render(request,"aboutpage.html")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        account = request.POST.get('account')
        message = request.POST.get('message')

        # Create a new Registration instance and save it to the database
        registration_instance = Registration(
            name=name,
            email=email,
            phone_number=phone_number,
            account=account,
            message=message
        )
        registration_instance.save()

        print("We will call you back.")

        # Redirect to a success page or any other appropriate action
        #return redirect('index.html')  # Replace 'success_page' with your actual success page URL

    return render(request, 'index.html')  # Replace 'registration_form.html' with your actual registration form template


#def register(request):
    return render(request,"/register.py")

#def register(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone_number=request.POST.get('phone_number')
    account=request.POST.get('account')
    message=request.POST.get('message')
    print(name)
    
    return render(request,"index.html")
