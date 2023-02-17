from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import logout

@login_required
def flux(request: HttpRequest):

    print("User is none (after redirect) : " + str(request.user is None))
    print("User isautheticated : " + str(request.user.is_authenticated))

    user: str = "User is none"

    if request.user.is_authenticated:
        user = "username : " + request.user.username

    return render(request, 'flux.html', {'user':user})

@login_required
def deconection(request: HttpRequest):
    logout(request)
    return redirect('login')    



