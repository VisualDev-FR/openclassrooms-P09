from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from factory.forms import TicketForm, ReviewForm
from LITReview.models import Ticket

@login_required
def create_ticket(request: HttpRequest):
    
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():            
            form.instance.user = request.user
            # form.instance.image.save()
            form.save()
            return redirect('feed')
    else:
        form = TicketForm()
    
    return render(request, 'new_ticket.html', {'form': form})


@login_required
def create_review(request: HttpRequest, ticket_pk: int = -1):

    if request.method == 'POST':

        ticket_form = TicketForm(request.POST or None)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            
            # create the new ticket
            ticket_form.instance.user = request.user
            ticket = ticket_form.save()
            
            # create the new review from the created ticket
            review_form.instance.user = request.user
            review_form.instance.ticket = ticket
            review_form.save()

            return redirect('feed')

        elif review_form.is_valid() and ticket_pk != -1:

            # create new review from ticket's pk 
            review_form.instance.user = request.user
            review_form.instance.ticket = Ticket.objects.get(pk=ticket_pk)
            review_form.save()

            return redirect('feed')
        
        else:
            #TODO: handle errors
            pass

        
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    if ticket_pk > -1:
        existing_ticket = Ticket.objects.get(pk=ticket_pk)
        ticket_form = None

        if existing_ticket.image.name.startswith('http'):
            image_url = existing_ticket.image.name
        
        elif existing_ticket.image.name != "":
            image_url = existing_ticket.image.url
        
        else:
            image_url = ""

    else:
        existing_ticket = None
        image_url = ""

    return render(
        request=request,
        template_name='new_review.html',
        context= {
            'review_form':review_form,
            'ticket_form':ticket_form,
            'existing_ticket':existing_ticket,
            'image_url':image_url
        }
    )
