from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib.auth import logout
from django.db.models import CharField, Value
from LITReview.models import Ticket, Review, UserFollows
from django.contrib.auth.models import User
from itertools import chain
import typing


def get_viewable_users(user: User) -> typing.List[User]:

    viewable_users = [user]
    viewable_users.extend(
        [userfollow.followed_user for userfollow in UserFollows.objects.filter(user=user)]
    )

    return viewable_users


def get_users_viewable_reviews(request: HttpRequest):

    viewable_users = get_viewable_users(request.user)   # type: ignore
    viewable_reviews = Review.objects.filter(user__in=viewable_users)

    return viewable_reviews.annotate(content_type=Value('REVIEW', CharField()))


def get_users_viewable_tickets(request: HttpRequest):

    viewable_users = get_viewable_users(request.user)   # type: ignore
    viewable_tickets = Ticket.objects.filter(user__in=viewable_users)

    return viewable_tickets.annotate(content_type=Value('TICKET', CharField()))


@login_required
def feed(request: HttpRequest):

    # returns annotated queryset of reviews
    reviews = set(get_users_viewable_reviews(request))

    # returns annotated queryset of tickets
    tickets = set(get_users_viewable_tickets(request))

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
