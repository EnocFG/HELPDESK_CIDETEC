from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class EstatusViewSet(viewsets.ModelViewSet):
    queryset = models.status_e.objects.all()
    serializer_class = serializers.EstatusSerializer