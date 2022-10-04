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
