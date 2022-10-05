from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class areaViewSet(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = areaSerializer


class proyectoViewSet(viewsets.ModelViewSet):
    queryset = proyecto.objects.all()
    serializer_class = proyectoSerializer


class rolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    serializer_class = rolSerializer


class espViewSet(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = espSerializer


class prioViewSet(viewsets.ModelViewSet):
    queryset = prioridad.objects.all()
    serializer_class = prioSerializer


class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer


class especViewSet(viewsets.ModelViewSet):
    queryset = especialista.objects.all()
    serializer_class = especSerializer


class probViewSet(viewsets.ModelViewSet):
    queryset = problemas.objects.all()
    serializer_class = probSerializer


class ticketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketSerializer

class estatusViewSet(viewsets.ModelViewSet):
    queryset = status.objects.all()
    serializer_class = estaSerializer