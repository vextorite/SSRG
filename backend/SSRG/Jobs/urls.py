from django.urls import path
from django.views.generic import TemplateView
from . import views

appName = "Jobs"

urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('register', views.registerRequest, name = 'register'),
     path('login', views.loginRequest, name='login'),
     path('logout', views.logoutRequest, name='logout'),
     path('newJob', views.newJob, name='new')
]
