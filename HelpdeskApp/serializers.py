from .models import *
from rest_framework import serializers


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status_e
        fields = '__all__'


class areaSerializer(serializers.ModelSerializer):
    class Meta:
        model = area
        fields = '__all__'


class proyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = proyecto
        fields = '__all__'


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'


class espSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
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


class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'


class EstatusTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = status_ticket
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentario
        fields = '__all__'


class HistorialTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial_ticket
        fields = '__all__'
