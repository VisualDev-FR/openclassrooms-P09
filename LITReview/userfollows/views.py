from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from userfollows.forms import FollowForm
from LITReview.models import UserFollows

@login_required
def userfollows(request: HttpRequest):

    if request.method == 'POST':

        follow_form = FollowForm(request.POST)

        if follow_form.is_valid():
            follow_form.instance.user = request.user
            follow_form.save()

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
