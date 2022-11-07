from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

#Vista para mostrar todos los tickets
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

#Vista para obtener solamente un ticket determinado
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

    def patch(self, request, id):
        p = self.get_object(id)
        serial = ticketSerializer(p, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_202_ACCEPTED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


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

class ComentarioView(APIView):
    def get(self, request):
        comentarios = comentario.objects.all().order_by('id')
        cs = ComentarioSerializer(comentarios, many=True)
        return Response(cs.data)
    def post(self, request):
        cs = ComentarioSerializer(data=request.data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_201_CREATED)
        return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)

class ComentarioDetalle(APIView):
    def get_object(self, id):
        try:
            return comentario.objects.get(id=id)
        except comentario.DoesNotExist:
            raise Http404
    def get(self, request, id):
        c = self.get_object(id)
        cs = ComentarioSerializer(c)
        return Response(cs.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        c = self.get_object(id)
        cs = ComentarioSerializer(c, data=request.data)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_200_OK)
        return Response(cs.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        c = self.get_object(id)
        cs = ComentarioSerializer(c, data=request.data, partial=True)
        if cs.is_valid():
            cs.save()
            return Response(cs.data, status=status.HTTP_202_ACCEPTED)

class EspecialistaView(APIView):
    def get(self, request):
        es = especialista.objects.all()
        es_se= especSerializer(es, many=True)
        return Response(es_se.data, status=status.HTTP_200_OK)

    def post(self, request):
        es_se = especSerializer(data=request.data)
        if es_se.is_valid():
            es_se.save()
            return Response(es_se.data, status=status.HTTP_201_CREATED)
        return Response(es_se.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(id):
        try:
            return especialista.objects.get(id=id)
        except especialista.DoesNotExist:
            raise Http404
class EspecDetalle(APIView):
    def get(self, request, id):
        e = get_object(id)
        es = especSerializer(e)
        return Response(es.data, status=status.HTTP_200_OK)
    def put(self, request, id):
        e = get_object(id)
        es = especSerializer(e, data=request.data)
        if es.is_valid():
            es.save()
            return Response(es.data, status=status.HTTP_202_ACCEPTED)
        return Response(es.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, id):
        e = get_object(id)
        es = especSerializer(e, data=request.data, partial=True)
        if es.is_valid():
            es.save()
            return Response(es.data, status=status.HTTP_202_ACCEPTED)
        return Response(es.errors, status=status.HTTP_400_BAD_REQUEST)
