"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views as LITReview
from feed import views as feed
from factory import views as factory
from userfollows import views as follows
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LITReview.login, name='login'),
    path('register/', LITReview.register, name='register'),
    path('logout/', LITReview.deconection, name='logout'),
    path('feed/', feed.feed, name='feed'),
    path('posts/', feed.posts, name='posts'),
    path('new_ticket', factory.create_ticket, name='new_ticket'),
    path('new_review/', factory.create_review, name='new_review'),
    path('new_review/<int:ticket_pk>', factory.create_review, name='new_review'),
    path('edit_ticket/<int:ticket_pk>', factory.edit_ticket, name='edit_ticket'),
    path('edit_review/<int:review_pk>', factory.edit_review, name='edit_review'),
    path('delete_ticket/<int:ticket_pk>', factory.delete_ticket, name='delete_ticket'),
    path('delete_review/<int:review_pk>', factory.delete_review, name='delete_review'),
    path('follows/', follows.follow_user, name='follows'),
    path('unfollow/<str:username>', follows.unfollow_user, name='unfollow'),
    path('followable_users/', follows.get_followable_usernames, name='followable_users')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
