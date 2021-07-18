from awwardsapp.models import Profile, Project, Rating
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import ModelState
from django.forms import fields

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user  



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'projects']
             

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user','project','average' 'date']        