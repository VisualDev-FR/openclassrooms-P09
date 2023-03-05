from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import auth
from LITReview.forms import LoginForm, RegisterForm


def login(request: HttpRequest):

    if request.method == 'POST':
        # parse received username and password
        form = LoginForm(request.POST)
        username: str = request.POST['username']
        password: str = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            auth.login(request, user)
            return redirect('feed')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request: HttpRequest):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'register.html', {'form': form})
