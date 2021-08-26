from typing_extensions import ParamSpecKwargs
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUser, SubmitJob
from .models import Jobs
from subprocess import run, PIPE
import sys

# Create your views here.
def homepage(request):
    return render(request=request, template_name='Jobs/home.html', context={'jobs': Jobs.objects.all})

def registerRequest(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #messages.success(request, "Success")
            return redirect("homepage")

    form = NewUser()
    return render(request = request, template_name="Jobs/register.html", context={'registration':form})

def loginRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, "Success")
                return redirect("homepage")
    form = AuthenticationForm()
    return render(request=request, template_name="Jobs/login.html", context={'login':form})

def logoutRequest(request):
    logout(request)
    return redirect("homepage")

def newJob(request):
    #form = SubmitJob()
    if request.method == 'POST':
        form = SubmitJob(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            form.instance.user = request.user
            
            arguments = [form.instance.user.username, 
                        form.instance.language,
                        form.instance.baseFile, 
                        form.instance.user.email]
            job.save()
            #run([sys.executable,
            #"//home//vextorite//Documents//Capstone-SSRG//ssrg-ndxsas021-hlnsan005-rmrsuv002//MossBackendJobs//test.py", 
            #arguments[0], arguments[1], arguments[2], arguments[3]])
            
            return redirect("homepage")
    else:
        form = SubmitJob()
    return render(request=request, template_name="Jobs/newJob.html", context={'submission': form})
