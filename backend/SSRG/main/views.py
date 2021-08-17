from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
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
            return redirect("main:homepage")
    form = NewUser()
    return render(request = request, template_name="registerTemplateHere", context={'registration':form})

