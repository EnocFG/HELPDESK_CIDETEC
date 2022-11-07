from .models import *
from rest_framework import serializers


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = estatus_e
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
    class Meta:
        model = especialista
        fields = '__all__'


class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'


class EstatusTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = estatus_ticket
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = comentario
        fields = '__all__'


class ejemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = ejemplo
        fields = '__all__'
