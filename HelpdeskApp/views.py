from .models import *
from .serializers import *
from rest_framework import viewsets


# Create your views here.
class EstatusViewSet(viewsets.ModelViewSet):
    queryset = status_e.objects.all()
    serializer_class = EstatusSerializer


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


class ticketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketSerializer


class EstatusTicketViewSet(viewsets.ModelViewSet):
    queryset = status_ticket.objects.all()
    serializer_class = EstatusTicketSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer


class HistorialViewSet(viewsets.ModelViewSet):
    queryset = historial_ticket.objects.all()
    serializer_class = HistorialTicketSerializer
