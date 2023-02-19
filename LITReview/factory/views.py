from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest


@login_required
def create_ticket(request: HttpRequest):
    pass


@login_required
def create_review(request: HttpRequest):
    pass
