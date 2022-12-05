from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from .forms import CustomUserCreationForm

def profile(request): 
    return render(request, 'profile.html')
def home(request): 
    return render(request, 'profile.html')