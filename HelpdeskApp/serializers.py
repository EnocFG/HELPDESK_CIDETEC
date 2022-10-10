from .models import *
from rest_framework import serializers


class EstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status_e
        fields = '__all__'
