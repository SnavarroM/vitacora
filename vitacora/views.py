from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.
def login(request):
    return render(request,'registration/login.html')



@login_required
def home(request):
    return render(request,'vitacora/home.html')


def index(request):
    return render(request,'vitacora/index.html')