from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from factory.forms import TicketForm


@login_required
def create_ticket(request: HttpRequest):
    
    if request.method == 'POST':
        form: TicketForm = TicketForm(request.POST)

        form.instance.user = request.user

        if form.is_valid():
            form.save()
    else:
        form = TicketForm()
    
    return render(request, 'new_ticket.html', {'form': form})


@login_required
def create_review(request: HttpRequest):
    return render(request, 'new_review.html')
