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


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'


class espSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = '__all__'


class estaSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = '__all__'


class prioSerializer(serializers.ModelSerializer):
    class Meta:
        model = prioridad
        fields = '__all__'


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'


class especSerializer(serializers.ModelSerializer):
    id_usuario = serializers.CharField(source='usuario.nombre_usuario')
    class Meta:
        model = especialista
        fields = '__all__'


class probSerializer(serializers.ModelSerializer):
    class Meta:
        model = problemas
        fields = '__all__'


class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'
