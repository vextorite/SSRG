from typing_extensions import ParamSpecKwargs
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUser
from .models import Jobs

# Create your views here.
def homepage(request):
    return render(request=request, template_name='main/home.html', context={'jobs': Jobs.objects.all})

def registerRequest(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #messages.success(request, "Success")
            return redirect("homepage")

    form = NewUser()
    return render(request = request, template_name="main/register.html", context={'registration':form})

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
    return render(request=request, template_name="main/login.html", context={'login':form})

def logoutRequest(request):
    logout(request)
    return redirect("homepage")