from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth.models import User

from login.forms import LoginForm, RegisterForm

def login(request: HttpRequest):

    if request.method == 'POST':
        # parse received username and password
        form = LoginForm(request.POST)        
        username: str = request.POST['username']
        password: str = request.POST['password']

        user: User = auth.authenticate(username=username, password=password)

        print("user is none (before redirect): " + str(user is None))

        if user is not None:
            # A backend authenticated the credentials
            auth.login(request, user)
            return redirect('flux')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})


def register(request: HttpRequest):

    form = RegisterForm()    

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')


    return render(request, 'signin.html', {'form':form})

    
