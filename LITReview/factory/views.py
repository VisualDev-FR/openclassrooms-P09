from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from factory.forms import TicketForm, ReviewForm
from LITReview.models import Ticket, Review


@login_required
def create_ticket(request: HttpRequest):

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('feed')
    else:
        form = TicketForm()

    return render(request, 'new_ticket.html', {
        'form': form,
        'title': "Créer un ticket"
    })


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
            # TODO: handle errors
            pass

    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    if ticket_pk > -1:
        existing_ticket = Ticket.objects.get(pk=ticket_pk)
        ticket_form = None

    else:
        existing_ticket = None

    return render(
        request=request,
        template_name='new_review.html',
        context={
            'review_form': review_form,
            'ticket_form': ticket_form,
            'existing_ticket': existing_ticket,
            'title': 'Créer une critique'
        }
    )


@login_required
def edit_ticket(request: HttpRequest, ticket_pk: int):

    ticket = Ticket.objects.get(pk=ticket_pk)

    # prevent the user to modify ticket not created by him
    if ticket.user != request.user:
        return redirect('posts')

    if request.method == 'POST':

        form = TicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'new_ticket.html', {
        'form': form,
        'ticket': ticket,
        'title': "Modifier votre ticket"
    })


@login_required
def edit_review(request: HttpRequest, review_pk: int):

    review = Review.objects.get(pk=review_pk)
    existing_ticket = review.ticket

    # prevent the user to modify review not created by him
    if review.user != request.user:
        return redirect('posts')

    if request.method == 'POST':

        review_form = ReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review_form.save()
            return redirect('posts')

    else:
        review_form = ReviewForm(instance=review)
        existing_ticket = review.ticket

    return render(
        request=request,
        template_name='new_review.html',
        context={
            'review_form': review_form,
            'existing_ticket': existing_ticket,
            'title': 'Modifier votre critique'
        }
    )


@login_required
def delete_ticket(request: HttpRequest, ticket_pk: int):

    ticket = Ticket.objects.get(pk=ticket_pk)

    # prevent the user to delete ticket not created by him
    if ticket.user == request.user:
        ticket.delete()

    return redirect('posts')


@login_required
def delete_review(request: HttpRequest, review_pk: int):

    review = Review.objects.get(pk=review_pk)

    # prevent the user to modify review not created by him
    if review.user == request.user:
        review.delete()

    return redirect('posts')
