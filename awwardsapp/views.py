from django.http.response import HttpResponseRedirect
from awwardsapp.forms import RegistrationForm, UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.http import request

from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    

    return render(request,'index.html')
       

# def profile(request):
#     username=request.user
#     user_prof = get_object_or_404(User, username=username)
#     if request.user == user_prof:
#         return redirect('profile')
#     params = {
#         'user_prof': user_prof,
#     }
#     return render(request, 'user/profile.html', params)

@login_required(login_url='/accounts/login/')
def profile(request):
 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:        
        profile_form = UserProfileForm(instance=request.user)
        user_form =UserForm(instance=request.user)         
    return render(request,'user/profile.html',{"user_form":user_form,"profile_form": profile_form}) 

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


