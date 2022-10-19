from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework import permissions
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class EstatusViewSet(viewsets.ModelViewSet):
    queryset = status_e.objects.all()
    serializer_class = EstatusSerializer
    permission_classes_by_action = {
        'create': (permissions.IsAdminUser,),
        'list': (permissions.IsAdminUser,),
        'retrieve': (permissions.IsAdminUser,),
        'update': (permissions.IsAdminUser,),
        'destroy': (permissions.IsAdminUser,),
        'search': (permissions.IsAdminUser,)  # <--- Option 1
    }


class areaViewSet(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = areaSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class proyectoViewSet(viewsets.ModelViewSet):
    queryset = proyecto.objects.all()
    serializer_class = proyectoSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class rolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    serializer_class = rolSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class espViewSet(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = espSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class prioViewSet(viewsets.ModelViewSet):
    queryset = prioridad.objects.all()
    serializer_class = prioSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class especViewSet(viewsets.ModelViewSet):
    queryset = especialista.objects.all()
    serializer_class = especSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class ticketViewSet(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticketSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class EstatusTicketViewSet(viewsets.ModelViewSet):
    queryset = status_ticket.objects.all()
    serializer_class = EstatusTicketSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class HistorialViewSet(viewsets.ModelViewSet):
    queryset = historial_ticket.objects.all()
    serializer_class = HistorialTicketSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
