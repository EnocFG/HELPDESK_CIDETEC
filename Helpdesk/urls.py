"""Helpdesk URL Configuration

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
from django.urls import path, include
from Profiles.views import SignUpView, BienvenidaView, SignInView, SignOutView
from django.conf import settings


urlpatterns = [
    #path('', BienvenidaView.as_view(), name='bienvenida'),
    path('admin/', admin.site.urls),
    path('', include('HelpdeskApp.urls')),
    path('registro/', SignUpView.as_view(), name='sign_up'),
    path('login/', SignInView.as_view(), name='sign_in'),
    path('logout/', SignOutView.as_view(), name='sign_out'),
    path('cuenta/', include('allauth.urls'), name='cuenta'),


]
