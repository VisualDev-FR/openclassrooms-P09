from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from login.forms import LoginForm, RegisterForm
from flux.views import flux

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError 
from django.contrib import messages


def login(request: HttpRequest):

    if request.method == 'POST':
        # parse received username and password
        form = LoginForm(request.POST)        
        username: str = request.POST['username']
        password: str = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            return redirect(flux)

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})


def register(request: HttpRequest):

    form = RegisterForm()    

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(login)


    return render(request, 'signin.html', {'form':form})