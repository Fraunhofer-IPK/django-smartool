# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import ArduinoResults  # Import your model
from django.http import JsonResponse

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def my_view(request):
    # Fetch data from the model
    data = ArduinoResults.objects.filter(ID__gt=0).values('ID', 'cycle_nr')
    
    return render(request, "home/index.html", {"data": data})

# Define a Django view function
def arduino_results_api(request):
    # Retrieve data from the ArduinoResults model
    data = list(
        ArduinoResults.objects.filter(ID__gt=0).values(
            'ID', 'cycle_nr', 'mean_ambient_temperature', 'mean_ambient_humidity',
            'mean_cavity_temperature', 'mean_cavity_pressure', 'mean_closing_force'
        )
    )

    # Return the data as a JSON response
    return JsonResponse(data, safe=False)



