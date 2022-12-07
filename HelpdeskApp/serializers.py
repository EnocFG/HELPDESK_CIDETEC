from .models import Ticket
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class TicketSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Ticket
        geo_field = "ubicacion"
        fields = '__all__'
