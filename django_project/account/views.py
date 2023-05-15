from math import log
import re
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
    
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


# Login Function If I Use it for preventing him from seeing containt just only if he logedin


# def Login(request):
#     if request.user.is_authenticated:
#         return render(request, "services.html")
#     else:
#         messages.info(request, "Please Login To Access This Page")
#         HttpResponseRedirect('index.html')

def LoginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('/services')
        else:
            messages.error(request, "Enter Your Data Correctly")

    # Add a default response for GET requests or when authentication fails
    return render(request, 'index.html')


def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or wherever you want
            return redirect('accounts/login/')
        else:
            # Handle invalid login credentials
            return redirect('accounts/login/')
    else:
        # Handle GET request or render the form
        return render(request, 'login.html')
