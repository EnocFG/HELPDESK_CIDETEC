from functools import partial
from sys import api_version
from tkinter.tix import Tree
from django.http import Http404, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import is_valid_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
import HelpdeskApp.models
from .serializers import *


# @csrf_exempt
# def TicketApi(request, id=0):
#     ticket = HelpdeskApp.models.ticket
#     if request.method == 'GET':
#         tickets = ticket.objects.all().order_by('id')
#         tickets_serializer = ticketSerializer(tickets, many=True)
#         return JsonResponse(tickets_serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         ticket_data = JSONParser().parse(request)
#         ticket_serializer = ticketSerializer(data=ticket_data)
#         if ticket_serializer.is_valid():
#             ticket_serializer.save()
#             return JsonResponse("Agregado exitosamente", safe=False)
#         return JsonResponse("Fallo al agregar", safe=False)
#
#     elif request.method == 'PUT':
#         ticket_data = JSONParser().parse(request)
#         t = ticket.objects.get(id=ticket_data['id'])
#         ticket_serializer = ticketSerializer(t, data=ticket_data)
#         if ticket_serializer.is_valid():
#             ticket_serializer.save()
#             return JsonResponse("Actualizado exitosamente", safe=False)
#         return JsonResponse("Fallo al actualizar", safe=False)
#
#     elif request.method == 'DELETE':
#         tickett = ticket.objects.get(id=id)
#         tickett.delete()
#         return JsonResponse("Eliminado exitosamente", safe=False)
#     return JsonResponse("Fallo al eliminar", safe=False)


@csrf_exempt
def ProyectoAPI(request, id=0):
    if request.method == 'GET':
        proyectos = proyecto.objects.all().order_by('id')
        proyectos_serializer = proyectoSerializer(proyectos, many=True)
        return JsonResponse(proyectos_serializer.data, safe=False)

    elif request.method == 'POST':
        proyecto_data = JSONParser().parse(request)
        proyecto_serial = proyectoSerializer(data=proyecto_data)
        if proyecto_serial.is_valid():
            proyecto_serial.save()
            return JsonResponse("Proyecto agregado", safe=False)
        else:
            errores = serializers.errors
            return JsonResponse("Error: " + errores, safe=False)

    elif request.method == 'PUT':
        proyecto_data = JSONParser().parse(request)
        Proyecto = proyecto.objects.get(id=proyecto_data['id'])
        proyecto_serial = proyectoSerializer(Proyecto, data=proyecto_data)
        if proyecto_serial.is_valid():
            proyecto_serial.save()
            return JsonResponse("Proyecto actualizado", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)

    elif request.method == 'DELETE':
        Proyecto = proyecto.objects.get(id=id)
        Proyecto.delete()
        return JsonResponse("Eliminado exitosamente", safe=False)
    return JsonResponse("Fallo al eliminar", safe=False)


@csrf_exempt
def AreaApi(request, id=0):
    if request.method == 'GET':
        a = area.objects.all().order_by('id')
        a_serializer = areaSerializer(a, many=True)
        return JsonResponse(a_serializer.data, safe=False)

    elif request.method == 'POST':
        a_data = JSONParser().parse(request)
        a_serializer = areaSerializer(data=a_data)
        if a_serializer.is_valid():
            a_serializer.save()
            return JsonResponse("Agregado exitosamente", safe=False)
        return JsonResponse("Fallo al agregar", safe=False)

    elif request.method == 'PUT':
        a_data = JSONParser().parse(request)
        a = area.objects.get(id=a_data['id'])
        a_serializer = ticketSerializer(a, data=a_data)
        if a_serializer.is_valid():
            a_serializer.save()
            return JsonResponse("Actualizado exitosamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)

    elif request.method == 'DELETE':
        t = HelpdeskApp.models.ticket.objects.get(id=id)
        t.delete()
        return JsonResponse("Eliminado exitosamente", safe=False)
    return JsonResponse("Fallo al eliminar", safe=False)


class UsuarioView(APIView):
    def get(self, request):
        usuarios = usuario.objects.all()
        serializer = usuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = usuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetalle(APIView):
    def get_object(self, id):
        try:
            return usuario.objects.get(id=id)
        except usuario.DoesNotExist:
            raise Http404

    def get(self, request, id):
        u = self.get_object(id)
        serial = usuarioSerializer(u)
        return Response(serial.data)

    def put(self, request, id):
        u = self.get_object(id)
        serial = usuarioSerializer(u, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        u = self.get_object(id)
        serial = usuarioSerializer(u, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketView(APIView):
    def get(self, request):
        tickets = ticket.objects.all()
        ts = ticketSerializer(tickets, many=True)
        return Response(ts.data)

    def post(self, request):
        ts = ticketSerializer(data=request.data)
        if ts.is_valid():
            ts.save()
            return Response(ts.data, status=status.HTTP_201_CREATED)
        return Response(ts.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(id):
    try:
        return ticket.objects.get(id=id)
    except ticket.DoesNotExist:
        raise Http404


class TicketDetalle(APIView):

    def get(self, request, id):
        t = get_object(id)
        ts = ticketSerializer(t)
        return Response(ts.data)

    def put(self, request, id):
        t = get_object(id)
        serial = usuarioSerializer(t, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        t = get_object(id)
        serial = usuarioSerializer(t, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class AreaView(APIView):
    def get(self, request):
        areas = area.objects.all()
        serial_area = areaSerializer(areas, many=True)
        return Response(serial_area.data)

    def post(self, request):
        serial_area = areaSerializer(data=request.data)
        if serial_area.is_valid():
            serial_area.save()
            return Response(serial_area.data, status=status.HTTP_201_CREATED)
        return Response(serial_area.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(id):
    try:
        return area.objects.get(id=id)
    except area.DoesNotExist:
        raise Http404


class AreaDetalle(APIView):
    def get(self, request, id):
        a = get_object(id)
        serial_area = areaSerializer(a)
        return Response(serial_area.data)

    def put(self, request, id):
        a = get_object(id)
        serial_area = areaSerializer(a, data=request.data)
        if serial_area.is_valid():
            serial_area.save()
            return Response(serial_area.data)
        return Response(serial_area.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        a = get_object(id)
        serial = usuarioSerializer(a, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

