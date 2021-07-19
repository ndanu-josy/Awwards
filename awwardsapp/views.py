from django.http.response import HttpResponseRedirect
from awwardsapp.forms import ProjectForm, RegistrationForm, UserForm, UserProfileForm,RatingForm
from django.contrib.auth.models import User
from django.http import request
from .models import Profile, Project, Rating
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView
# from .models import  MoringaMerch
from .serializer import ProfileSerializer, ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Rating.objects.all()
    return render(request,'index.html', {"profiles":profiles,"projects":projects, "reviews":reviews})
       

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

@login_required(login_url='/accounts/login')
def new_project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
            
			return redirect('index')
	else:
			form = ProjectForm()
         
	return render(request, 'project.html',{"form":form})


def searchproject(request): 
    if 'project' in request.GET and request.GET['project']:
        name = request.GET.get("project")
        searchResults = Project.search_projects(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any project"
    return render(request, 'search.html', {'message': message})


@login_required(login_url='/accounts/login')
def all_projects(request,id):
    project = Project.objects.get(id = id)
   
    reviews = Rating.objects.all()

    return render(request, 'all_projects.html',{"project":project, "reviews":reviews})    

@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    reviews = Rating()
    proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
           
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            reviews = Rating()
            reviews.project = project
            reviews.user = current_user
            reviews.design = design
            reviews.usability = usability
            reviews.content = content
            reviews.average = (reviews.design + reviews.usability + reviews.content)/3
            print(reviews.average)
            print(reviews.usability)
            reviews.save()

            # return redirect('index')
            return HttpResponseRedirect(reverse('allProjects', args=(project.id,)))
    else:
        form = RatingForm()
    return render(request, 'reviews.html', {"user":current_user,"project":proj,"form":form, "reviews":reviews })



class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
     
    permission_classes = (IsAdminOrReadOnly,)

class ProfileList(APIView):
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data) 

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)
           