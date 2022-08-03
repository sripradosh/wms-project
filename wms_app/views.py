from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def uav(request):
    return render(request, 'uav.html')


def cloud(request):
    return render(request, 'cloud.html')


def datadisplay(request):
    return render(request, 'datadisplay.html')


def about(request):
    return render(request, 'about.html')


def ourteam(request):
    return render(request, 'ourteam.html')