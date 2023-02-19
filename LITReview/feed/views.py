from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import logout

@login_required
def feed(request: HttpRequest):
    return render(request, 'feed.html')

@login_required
def deconection(request: HttpRequest):
    logout(request)
    return redirect('login')    



