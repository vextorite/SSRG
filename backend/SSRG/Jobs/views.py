from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, FileResponse
from .forms import NewUser, SubmitJob, Files, EditProfile
from .models import Jobs, SingleFiles
import os
from SSRG.celery import testTask

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'MossBackendJobs/jobRequest.py')

filename2 = os.path.split(dirname)
filename2 = os.path.join(filename2[0], 'jobs')

# Create your views here.
def homepage(request):
    """
    Routes to homepage
    Parameters
    ----------
    request: request
    """
    return render(request=request, template_name='Jobs/home.html')

@login_required(login_url='/login')
def menu(request):
    """
    Routes to menu
    Parameters
    ----------
    request: request
    """
    return render(request=request, template_name='Jobs/menu.html')

def registerRequest(request):
    """
    Routes to register
    Parameters
    ----------
    request: request
    """
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Success")
            return redirect("menu")

        messages.error(request, "Error! Invalid information or unsecure password.")
    form = NewUser()
    return render(request = request, template_name="Jobs/register.html", context={'registration':form})

def loginRequest(request):
    """
    Routes to login
    Parameters
    ----------
    request: request
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Login successful. Welcome {username}!")
                return redirect("menu")
            else:
                messages.error(request, "Invalid Username/Password combination")
        else:
            messages.error(request, "Invalid Username/Password combination")

    form = AuthenticationForm()
    return render(request=request, template_name="Jobs/login.html", context={'login':form})

def logoutRequest(request):
    """
    Routes to logout
    Parameters
    ----------
    request: request
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("homepage")

@login_required(login_url='/login')
def newJob(request):
    """
    Routes to submit a new job
    Parameters
    ----------
    request: request
    """
    basefileState = 'False'
    if request.method == 'POST':
        form = SubmitJob(request.POST)
        singleFilesForm = Files(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid() and singleFilesForm.is_valid():
            job = form.save(commit=False)
            form.instance.user = request.user
            job.save()
            for f in files:
                fileInstance = SingleFiles(files = f, jobInstance = job, user=request.user, slug = form.instance.slug)
                fileInstance.save()
            files = request.FILES.getlist('baseFile')
            if (len(files)==0):
                basefileState = 'False'
            else:
                basefileState = 'True'
            for f in files:
                fileInstance = SingleFiles(baseFile = f, jobInstance = job, user=request.user, slug = form.instance.slug)
                fileInstance.save()

            arguments = [form.instance.user.username, 
                        form.instance.language,
                        basefileState, 
                        form.instance.user.email,
                        form.instance.emailNow,
                        form.instance.slug,
                        f"{filename2}/{form.instance.user.username}/{form.instance.slug}"]
            testTask.delay(filename, arguments[0], arguments[5], arguments[1], arguments[2], arguments[3], arguments[4], arguments[6])            
            return redirect("menu")
    else:
        form = SubmitJob()
        singleFilesForm = Files()
    return render(request=request, template_name="Jobs/newJob.html", context={'submission': form, 'singles':singleFilesForm})

@login_required(login_url='/login')
def viewJobs(request):
    """
    Routes to view jobs
    Parameters
    ----------
    request: request
    """
    return render(request=request, template_name="Jobs/jobsSubmitted.html", context={'pendingJobs':Jobs.pendingJobObjects.filter(user=request.user), 'successJobs':Jobs.successJobObjects.filter(user=request.user), 'failedJobs':Jobs.failedJobObjects.filter(user=request.user)})

@login_required(login_url='/login')
def singleJobDetail(request, jobs):
    """
    Routes to job detail
    Parameters
    ----------
    request: request
    jobs: str
    """
    path = os.path.split(dirname)
    path = os.path.join(path[0], 'jobs')
   
    viewPath = f"{path}/{request.user}/{jobs}/final_landing.html"
    return FileResponse(open(viewPath, 'rb'))

@login_required(login_url='/login')
def JobDetail(request, filename):
    """
    Routes to MOSS generated files
    Parameters
    ----------
    request: request
    filename: str
    """
    viewPath = filename
    viewPath = viewPath.replace('~', '/')
    return FileResponse(open(viewPath, 'rb'))

@login_required(login_url='/login')
def reportView(request, jobs):
    """
    Routes to generated report
    Parameters
    ----------
    request: request
    jobs: str
    """
    path = os.path.split(dirname)
    path = os.path.join(path[0], 'jobs')
   
    reportPath = f"{path}/{request.user}/{jobs}/JobReport.pdf"
    return FileResponse(open(reportPath, 'rb'), content_type='application/pdf')

@login_required(login_url='/login')
def editUserDetails(request):
    """
    Routes to user options
    Parameters
    ----------
    request: request
    """
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfile(instance=request.user)
        return render(request=request, template_name='Jobs/profile.html', context={'form':form})
