from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


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

class TicketDetalle(APIView):
    def get_object(self, id):
        try:
            return ticket.objects.get(id=id)
        except ticket.DoesNotExist:
            raise Http404

    def get(self, request, id):
        t = self.get_object(id)
        serial = ticketSerializer(t)
        return Response(serial.data)

    def put(self, request, id):
        t = self.get_object(id)
        serial = ticketSerializer(t, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        t = self.get_object(id)
        serial = ticketSerializer(t, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class ProyectoView(APIView):
    def get(self, request):
        proyectos = proyecto.objects.all()
        ps = proyectoSerializer(proyectos, many=True)
        return Response(ps.data)

    def post(self, request):
        ps = proyectoSerializer(data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data, status=status.HTTP_201_CREATED)


class ProyectoDetalle(APIView):
    def get_object(self, id):
        try:
            return proyecto.objects.get(id=id)
        except proyecto.DoesNotExist:
            raise Http404

    def get(self, request, id):
        p = self.get_object(id)
        ps = proyectoSerializer(p)
        return Response(ps.data)

    def put(self, request, id):
        p = self.get_object(id)
        ps = proyectoSerializer(p)
        if ps.is_valid():
            ps.save()
            return Response(ps.data, status=status.HTTP_202_ACCEPTED)
        return Response(ps.errors, status=status.HTTP_400_BAD_REQUEST)


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
