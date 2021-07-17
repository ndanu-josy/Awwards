from awwardsapp.forms import RegistrationForm
from django.contrib.auth.models import User
from django.http import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    

    return render(request,'index.html')
       
@login_required(login_url='/accounts/login/')
def profile(request, username):
    user_profile= User.objects.get(username=username)
    id= request.user.id 
    form = UserProfileForm()

    return render(request,'index.html')
       

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 

