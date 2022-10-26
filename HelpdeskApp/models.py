from django.db import models
from .choices import roles
from .choices import prioridades
from .choices import status_tickets
from django.utils import timezone


# Clase status de las entidades correpondenes a proyecto, area, usuario, especialista
class status_e(models.Model):
    tipo_estatus = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField()


# Clase Proyecto
class proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=50)
    codigo_proyecto = models.CharField(max_length=5)
    fecha_inicial = models.DateTimeField(verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(verbose_name='Fecha final')
    descripcion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(
        status_e, null=True, blank=True, on_delete=models.CASCADE)


# Clase Area para la tabla Proyecto
class area(models.Model):
    nombre_area = models.CharField(max_length=10)
    codigo_area = models.CharField(max_length=5)
    descripcion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    area_proyecto = models.ManyToManyField(proyecto)
    status_entidad = models.ForeignKey(
        status_e, null=True, blank=True, on_delete=models.CASCADE)


# Clase Rol para la tabla Usuario


class rol(models.Model):
    tipo_rol = models.CharField(max_length=2, choices=roles, default='SA')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)


# Clase Especilidad para la tabla Especialista


class especialidad(models.Model):
    tipo_especialidad = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo_especialidad


# Clase Usuario


class usuario(models.Model):
    codigo_usuario = models.CharField(max_length=20)
    nombre_usuario = models.CharField(
        max_length=50, verbose_name='Nombre del usuario')
    apellidos_usuario = models.CharField(
        max_length=50, verbose_name='Apellidos del usuario')
    email_usuario = models.EmailField(verbose_name='Correo')
    password = models.CharField(max_length=8)
    usuario_rol = models.ForeignKey(
        rol, null=True, blank=True, on_delete=models.CASCADE)
    usuario_proyecto = models.ManyToManyField(proyecto)
    usuario_area = models.ManyToManyField(area)
    status_entidad = models.ForeignKey(
        status_e, null=True, blank=True, on_delete=models.CASCADE)


# class proyecto_usuario (models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)

# Clase Area_Usuario para relacionar las tablas áreas
# class area_usuario(models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     area = models.ForeignKey(area, on_delete=models.CASCADE)

# Clase Especialista para la tabla Especilidad
class especialista(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(
        status_e, null=True, blank=True, on_delete=models.CASCADE)
    especialista_especialidad = models.ForeignKey(
        especialidad, null=True, blank=True, on_delete=models.CASCADE)
    especialista_usuario = models.ManyToManyField(usuario)


# class especialistas_especialidades(models.Model):
#     especialista=models.ForeignKey(especialista, on_delete=models.CASCADE)
#     especialidades=models.ForeignKey(especialidad, on_delete=models.CASCADE)
# Clase para la tabla Prioridad


class prioridad(models.Model):
    tipo_prioridad = models.CharField(
        max_length=30, choices=prioridades, default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)


# Clase para la tabla que relaciona el Estatus y Ticket


class status_ticket(models.Model):
    tipo_estatus = models.CharField(
        max_length=10, choices=status_tickets, default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)


# Clase para la tabla del Ticket
class ticket(models.Model):
    folio = models.CharField(max_length=20)
    titulo = models.CharField(max_length=50)
    ticket_usariocreador = models.ForeignKey(
        usuario, null=True, blank=True, on_delete=models.CASCADE)
    ticket_especialistaasignado = models.ForeignKey(
        especialista, null=True, blank=True, on_delete=models.CASCADE)
    ticket_tipoprioridad = models.ForeignKey(
        prioridad, null=True, blank=True, on_delete=models.CASCADE)
    ticket_tipostatus = models.ForeignKey(
        status_ticket, null=True, blank=True, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=30, null=True)
    evidencias = models.ImageField(null=True)
    descripcion = models.TextField(null=True)
    ticket_proyecto = models.ForeignKey(
        proyecto, null=True, blank=True, on_delete=models.CASCADE)
    ticket_areaorigen = models.ForeignKey(
        area, null=True, blank=True, on_delete=models.CASCADE)
    comentario_t = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha creacion del ticket')
    fecha_atendido = models.DateTimeField(null=True, verbose_name='Fecha atendido')
    fecha_asignado = models.DateTimeField(null=True, verbose_name='Fecha asignado')
    fecha_proceso = models.DateTimeField(null=True, verbose_name='Fecha proceso')
    fecha_resuelto = models.DateTimeField(null=True, verbose_name='Fecha resuelto')
    fecha_validado = models.DateTimeField(null=True, verbose_name='Fecha validado')
    fecha_cancelado = models.DateTimeField(null=True, verbose_name='Fecha cancelado')
    ticket_superior = models.BigIntegerField(null=True)


# Clase para la tabla Comentario
class comentario(models.Model):
    comentario_usuario = models.ForeignKey(
        usuario, null=True, blank=True, on_delete=models.CASCADE, related_name='comentario')
    fecha_comentario = models.DateTimeField(default=timezone.now)
    comentario_ticket = models.ForeignKey(
        ticket, null=True, blank=True, on_delete=models.CASCADE)
    contenido_ticket = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField()


# Clase para la tabla del Historial del Ticket


class historial_ticket(models.Model):
    ht_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    ht_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(
        verbose_name='Fecha modificacion')
    status_anterior = models.ForeignKey(
        status_ticket, null=True, blank=True, on_delete=models.CASCADE)
    especialista_anterior = models.ForeignKey(
        especialista, null=True, blank=True, on_delete=models.CASCADE)
