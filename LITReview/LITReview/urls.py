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
from login import views as login
from feed import views as feed
from factory import views as factory
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login.login, name='login'),
    path('register/', login.register, name='register'),
    path('feed/', feed.feed, name='feed'),
    path('logout/', feed.deconection, name='logout'),
    path('new_ticket', factory.create_ticket, name='new_ticket'),
    path('new_review/', factory.create_review, name='new_review'),
    path('new_review/<int:ticket_pk>', factory.create_review, name='new_review'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
