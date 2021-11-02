from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import Userform

# Create your views here.


def welcome(request):
    return render(request, "welcome.html")

def login(request):
    form = Userform()
    return render(request, 'login.html', {'form': form})


def dashboard(request):
    return render(request, "dashboard.html")
        

def staffManagement(request):
    return render(request, "staffManagement.html")


def reports(request):
    return render(request, "reports.html")


def lab(request):
    return render(request, "lab.html")


def patients(request):
    return render(request, "registerPatient.html")
