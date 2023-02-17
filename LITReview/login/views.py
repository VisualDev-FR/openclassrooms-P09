# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')