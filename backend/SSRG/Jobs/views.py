from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUser, SubmitJob
from .models import Jobs
from subprocess import run, PIPE
import os, sys

# Create your views here.
def homepage(request):
    return render(request=request, template_name='Jobs/home.html', context={'jobs': Jobs.objects.all()})

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
                        form.instance.user.email,
                        form.instance.emailNow]
            job.save()
            os.system(
            f"python3 /home/Vextorite/Documents/Capstone/ssrg-ndxsas021-hlnsan005-rmrsuv002/backend/SSRG/Jobs/MossBackendJobs/jobRequest.py {arguments[0]} {arguments[1]} 'False' {arguments[2]} {arguments[3]} {arguments[4]}")
            
            return redirect("homepage")
    else:
        form = SubmitJob()
    return render(request=request, template_name="Jobs/newJob.html", context={'submission': form})

def viewJobs(request):
    return render(request=request, template_name="Jobs/jobsSubmitted.html", context={'pendingJobs':Jobs.pendingJobObjects.all(), 'successJobs':Jobs.successJobObjects.all(), 'failedJobs':Jobs.failedJobObjects.all()})

def singleJobDetail(request, jobs):

    jobs = get_object_or_404(Jobs, slug=jobs)
    return render(request=request, template_name="Jobs/jobDetails.html", context={'jobs':jobs})
