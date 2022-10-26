from rest_framework import viewsets
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from HelpdeskApp.models import ticket


@csrf_exempt
def TicketApi(request, id=0):
    if request.method == 'GET':
        tickets = ticket.objects.all()
        tickets_serializer = ticketSerializer(tickets, many=True)
        return JsonResponse(tickets_serializer.data, safe=False)

    elif request.method == 'POST':
        ticket_data = JSONParser().parse(request)
        ticket_serializer = ticketSerializer(data=ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse("Agregado exitosamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False)

    elif request.method == 'PUT':
        ticket_data = JSONParser().parse(request)
        ticket = ticket.objects.get(id=ticket_data['id'])
        ticket_serializer = ticketSerializer(ticket, data=ticket_data)
        if ticket_serializer.is_valid():
            ticket_serializer.save()
            return JsonResponse("Actualizado exitosamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)

    elif request.method == 'DELETE':
        ticket = ticket.objects.get(id=id)
        ticket.delete()
        return JsonResponse("Eliminado exitosamente", safe=False)
    return JsonResponse("Fallo al eliminar", safe=False)


class EstatusViewSet(viewsets.ModelViewSet):
    queryset = status_e.objects.all()
    serializer_class = EstatusSerializer
    # permission_classes_by_action = {
    #     'create': (permissions.IsAdminUser,),
    #     'list': (permissions.IsAdminUser,),
    #     'retrieve': (permissions.IsAdminUser,),
    #     'update': (permissions.IsAdminUser,),
    #     'destroy': (permissions.IsAdminUser,),
    #     'search': (permissions.IsAdminUser,)  # <--- Option 1
    # }


class areaViewSet(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = areaSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class proyectoViewSet(viewsets.ModelViewSet):
    queryset = proyecto.objects.all()
    serializer_class = proyectoSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class rolViewSet(viewsets.ModelViewSet):
    queryset = rol.objects.all()
    serializer_class = rolSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class espViewSet(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = espSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class prioViewSet(viewsets.ModelViewSet):
    queryset = prioridad.objects.all()
    serializer_class = prioSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class especViewSet(viewsets.ModelViewSet):
    queryset = especialista.objects.all()
    serializer_class = especSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


# class ticketViewSet(viewsets.ModelViewSet):
#     queryset = ticket.objects.all()
#     serializer_class = ticketSerializer
# permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class EstatusTicketViewSet(viewsets.ModelViewSet):
    queryset = status_ticket.objects.all()
    serializer_class = EstatusTicketSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = comentario.objects.all()
    serializer_class = ComentarioSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class HistorialViewSet(viewsets.ModelViewSet):
    queryset = historial_ticket.objects.all()
    serializer_class = HistorialTicketSerializer
    # permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]
