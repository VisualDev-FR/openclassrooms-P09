from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from LITReview.models import UserFollows
from django.contrib.auth.models import User


def get_followable_usernames(request: HttpRequest) -> JsonResponse:

    # create array of all followed users username
    followed_users = [
        User.objects.get(pk=follow.followed_user.pk).username 
        for follow in UserFollows.objects.filter(user=request.user.pk)
    ]

    # prevent the users to follow themself
    followed_users.append(request.user.username)

    # request all users who can be followed to database
    followable_users = [user.username for user in User.objects.exclude(username__in=followed_users)]

    return JsonResponse(followable_users, safe=False)


@login_required
def render_follow_page(request: HttpRequest) -> HttpResponse:

    # update the follows infos
    followed_users = [follow.followed_user.username for follow in UserFollows.objects.filter(user=request.user.pk)]
    followers = [follow.user.username for follow in UserFollows.objects.filter(followed_user=request.user.pk)]

    # render the follow page
    return render(
        request,
        'follows.html', 
        {
            'followed_users':followed_users,
            'followers':followers
        }
    )


@login_required
def follow_user(request: HttpRequest):

    if request.method == 'POST':
        try:
            followed_username = request.POST.get('followed_user')
            
            # prevent the users to follow themself
            if followed_username != request.user.username: 
                uf = UserFollows(
                    user = request.user,
                    followed_user = User.objects.get(username=followed_username)
                )
                uf.save()

        except:
            pass

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
