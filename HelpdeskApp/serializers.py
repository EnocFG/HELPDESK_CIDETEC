from .models import *
from rest_framework import serializers


class areaSerializer(serializers.ModelSerializer):
    class Meta:
        model = area
        fields = ['id', 'nombre_area', 'codigo_area', 'id_proyecto']


class proyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = proyecto
        fields = ['id', 'nombre_proyecto', 'codigo_proyecto', 'fecha_inicio', 'fecha_culminacion', 'descripcion']
