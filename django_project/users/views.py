from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import ExtendedUserCreationForm

def newsignup(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:
                    saveuser = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        email=form.cleaned_data['email']
                    )
                    saveuser.save()
                    return render(request, 'signup_pop.html', {
                        "form": ExtendedUserCreationForm(),
                        "info": "The user "+form.cleaned_data['username']+" was created successfully."
                    })
                except IntegrityError:
                    return render(request, 'signup_pop.html', {
                        "form": ExtendedUserCreationForm(),
                        "info": "The user "+form.cleaned_data['username']+" already exists."
                    })
            else:
                return render(request, 'signup_pop.html', {
                    "form": ExtendedUserCreationForm(),
                    "error": "The passwords do not match."
                })
    else:
        form = ExtendedUserCreationForm()
    
    return render(request, 'signup_pop.html', {"form": form})

from django.contrib.auth.forms import AuthenticationForm
from .forms import ExtendedUserCreationForm

def newlogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']  # Retrieve email from the 'username' field
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('services') 
            else:
                return render(request, 'login_popup.html', {
                    'form': form,
                    'error': 'Invalid email or password.',
                })
    else:
        form = AuthenticationForm()

    return render(request, 'login_popup.html', {'form': form})


def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('index.html')
