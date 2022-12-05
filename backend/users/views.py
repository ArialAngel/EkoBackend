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

def signup(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('/signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
    