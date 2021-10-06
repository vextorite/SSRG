from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

appName = "Jobs"
'''
URL routing
'''


urlpatterns = [
     path('', views.homepage, name='homepage'),
     path('viewReport/<filename>',views.JobDetail, name='misc'),
     path('register', views.registerRequest, name = 'register'),
     path('login', views.loginRequest, name='login'),
     path('logout', views.logoutRequest, name='logout'),
     path('password/', auth_views.PasswordChangeView.as_view(template_name='Jobs/changePassword.html')),
     path('newJob', views.newJob, name='new'),
     path('viewJobs', views.viewJobs, name='viewJobs'),
     path('menu', views.menu,name='menu'),
     path('report/<slug:jobs>', views.reportView, name='report'),
     path('details/<slug:jobs>', views.singleJobDetail, name='jobDetail'),
     path('profile', views.editUserDetails, name='profile')
]
