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
from rest_framework import routers
from HelpdeskApp import views

router = routers.DefaultRouter()
router.register(r'area', views.areaViewSet)
router.register(r'proyecto', views.proyectoViewSet)
router.register(r'rol', views.rolViewSet)
router.register(r'especialidad', views.espViewSet)
router.register(r'prioridad', views.prioViewSet)
router.register(r'usuario', views.usuarioViewSet)
router.register(r'especialista', views.especViewSet)
router.register(r'ticket', views.ticketViewSet)
router.register(r'estatus', views.EstatusViewSet)
router.register(r'estatus_ticket', views.EstatusTicketViewSet)
router.register(r'comentario', views.ComentarioViewSet)
router.register(r'historial_ticket', views.HistorialViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
