from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.db.models import CharField, Value
from LITReview.models import Ticket, Review, UserFollows
from django.contrib.auth.models import User
from itertools import chain
from django.db.models import Q
import typing


def get_viewable_users(user: User) -> typing.List[User]:

    viewable_users = [user]
    viewable_users.extend(
        [userfollow.followed_user for userfollow in UserFollows.objects.filter(user=user)]
    )

    return viewable_users


def get_users_viewable_reviews(request: HttpRequest):

    viewable_users = get_viewable_users(request.user)   # type: ignore
    viewable_reviews = Review.objects.filter(Q(user__in=viewable_users) | Q(ticket__user=request.user))

    return viewable_reviews.annotate(content_type=Value('REVIEW', CharField()))


def get_users_viewable_tickets(request: HttpRequest):

    viewable_users = get_viewable_users(request.user)   # type: ignore
    viewable_tickets = Ticket.objects.filter(user__in=viewable_users)

    return viewable_tickets.annotate(content_type=Value('TICKET', CharField()))


def get_currentUser_reviews(request: HttpRequest):
    return Review.objects.filter(user=request.user).annotate(content_type=Value('REVIEW', CharField()))


def get_currentUser_tickets(request: HttpRequest):
    return Ticket.objects.filter(user=request.user).annotate(content_type=Value('TICKET', CharField()))


def get_posts(reviews, tickets):
    return sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )


@login_required
def feed(request: HttpRequest):

    # returns annotated queryset of reviews
    reviews = set(get_users_viewable_reviews(request))

    # returns annotated queryset of tickets
    tickets = set(get_users_viewable_tickets(request))

    for ticket in tickets:
        ticket.is_reviewable = not Review.objects.filter(ticket=ticket, user=request.user).exists()  # type: ignore

    return render(request, 'feed.html', context={'posts': get_posts(reviews, tickets), 'user': request.user})


@login_required
def posts(request: HttpRequest):

    reviews = get_currentUser_reviews(request)
    tickets = get_currentUser_tickets(request)

    return render(request, 'post.html', context={'posts': get_posts(reviews, tickets)})
