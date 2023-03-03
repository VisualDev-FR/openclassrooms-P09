from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import logout
from django.db.models import CharField, Value
from django.shortcuts import render

from LITReview.models import Ticket, Review

from itertools import chain
import typing

@login_required
def get_users_viewable_reviews(request: HttpRequest):
    return Review.objects.filter(user=request.user.pk).annotate(content_type=Value('REVIEW', CharField()))


@login_required
def get_users_viewable_tickets(request: HttpRequest):
    return Ticket.objects.filter(user=request.user.pk).annotate(content_type=Value('TICKET', CharField()))


@login_required
def feed(request: HttpRequest):

    # returns annotated queryset of reviews
    reviews = get_users_viewable_reviews(request)

    # returns annotated queryset of tickets
    tickets = get_users_viewable_tickets(request)

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'feed.html', context={'posts': posts})

@login_required
def deconection(request: HttpRequest):
    logout(request)
    return redirect('login')    
