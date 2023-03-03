from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from userfollows.forms import FollowForm
from LITReview.models import UserFollows
from django.contrib.auth.models import User


@login_required
def render_follow_page(request: HttpRequest) -> HttpResponse:
    # force the reset of the form
    follow_form = FollowForm()

    # update the follows infos
    followed_users = [follow.followed_user.username for follow in UserFollows.objects.filter(user=request.user.pk)]
    followers = [follow.user.username for follow in UserFollows.objects.filter(followed_user=request.user.pk)]

    # render the follow page
    return render(
        request,
        'follows.html', 
        {
            'follow_form':follow_form,
            'followed_users':followed_users,
            'followers':followers
        }
    )


@login_required
def follow_user(request: HttpRequest):

    if request.method == 'POST':

        follow_form = FollowForm(request.POST)

        if follow_form.is_valid():
            follow_form.instance.user = request.user
            follow_form.save()
            return redirect('follows')

    return render_follow_page(request)


@login_required
def unfollow_user(request: HttpRequest, username: str):

    if request.method == 'POST':
        user_followed_pk = User.objects.get(username=username).pk
        user_follow = UserFollows.objects.get(user=request.user.pk, followed_user=user_followed_pk)
        user_follow.delete()

        return redirect('follows')
    
    return render_follow_page(request)
