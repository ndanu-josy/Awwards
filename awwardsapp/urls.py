from django.conf.urls import include, url
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[  
    url(r'^$',views.index,name='index'),
    url(r'register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'profile/', views.profile, name='profile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^PostImage/$',views.new_project,name='new-project'),
  
    url(r'^project_details/(?P<id>\d+)', views.all_projects, name='allProjects'),
    
    url(r'^review/(?P<project_id>\d+)', views.review_project, name='review'),
    url('search/', views.searchproject, name='search'),
    url(r'^api/projectApi/$', views.ProjectList.as_view()),
    url(r'^api/profileApi/$', views.ProfileList.as_view()),
      url(r'^api-token-auth/', obtain_auth_token),
]