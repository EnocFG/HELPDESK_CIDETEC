from django.db import models
from .choices import status_entidades
from .choices import roles
from .choices import prioridades
from .choices import status_tickets


from django.utils import timezone


# Clase status de las entidades correpondenes a proyecto, area, usuario, especialista
class status_e(models.Model):

    tipo_estatus = models.CharField(max_length=30, choices=status_entidades, default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha incial')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha final')

# Clase Proyecto
class proyecto(models.Model):

    nombre_proyecto = models.CharField(max_length=50)
    codigo_proyecto = models.CharField(max_length=10, unique=True)
    fecha_inicial = models.DateTimeField(auto_now_add=True, verbose_name='Fecha incial del proyecto')
    fecha_final = models.DateTimeField(auto_now=True, verbose_name='Fecha final del proyecto')
    descripcion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_proyecto

#Clase Area para la tabla Proyecto
class area(models.Model):

    nombre_area = models.CharField(max_length=10)
    codigo_area = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    area_proyecto = models.ManyToManyField(proyecto)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_area

#Clase Rol para la tabla Usuario
class rol(models.Model):
    tipo_rol = models.CharField(max_length=2, choices=roles, default='SA')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tipo_rol

#Clase Especilidad para la tabla Especialista
class especialidad (models.Model):
    tipo_especialidad = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    proyecto_especialidad = models.ForeignKey(proyecto, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.tipo_especialidad
#Clase Usuario
class usuario(models.Model):

    codigo_usuario = models.CharField(max_length=20, unique=True)
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del usuario')
    apellidos_usuario = models.CharField(max_length=50, verbose_name='Apellidos del usuario')
    email_usuario = models.EmailField(unique=True, verbose_name='Correo electrónico')
    password = models.CharField(max_length=8, verbose_name='Ingrese su contraseña')
    usuario_rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)
    usuario_proyecto = models.ManyToManyField(proyecto)
    usuario_area = models.ManyToManyField(area)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario_rol
    def __str__(self):
        return self.usuario_proyecto
    def __str__(self):
        return self.usuario_area


# class proyecto_usuario (models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)

#Clase Area_Usuario para relacionar las tablas áreas
# class area_usuario(models.Model):
#     usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     area = models.ForeignKey(area, on_delete=models.CASCADE)

#Clase Especialista para la tabla Especilidad
class especialista(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)
    especialista_especialidad = models.ManyToManyField(especialidad, null=True, blank=True, on_delete=models.CASCADE)
    especialista_usuario = models.ManyToManyField(usuario)


# class especialistas_especialidades(models.Model):
#     especialista=models.ForeignKey(especialista, on_delete=models.CASCADE)
#     especialidades=models.ForeignKey(especialidad, on_delete=models.CASCADE)
# Clase para la tabla Prioridad
class prioridad(models.Model):
    tipo_prioridad = models.CharField(max_length=30, choices=prioridades, default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tipo_prioridad

# Clase para la tabla que relaciona el Estatus y Ticket
class status_ticket(models.Model):
    tipo_estatus = models.CharField(max_length=10, choices=status_tickets, default='1')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tipo_estatus

# Clase para la tabla del Ticket
class ticket(models.Model):
    folio = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=5)
    ticket_usariocreador = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE)
    ticket_especialistaasignado = models.ForeignKey(especialista, null=True, blank=True, on_delete=models.CASCADE)
    ticket_tipoprioridad = models.ForeignKey(prioridad, null=True, blank=True, on_delete=models.CASCADE)
    ticket_tipostatus = models.ForeignKey(status_ticket, null=True, blank=True, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=30)
    evidencias = models.ImageField()
    descripcion = models.TextField(null=True)
    ticket_proyecto = models.ForeignKey(proyecto, null=True, blank=True, on_delete=models.CASCADE)
    ticket_areaorigen = models.ForeignKey(area, null=True, blank=True, on_delete=models.CASCADE)
    comentario_t = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion del ticket')
    fecha_atendido = models.DateTimeField(default=True,verbose_name='Fecha atendido')
    fecha_asignado = models.DateTimeField(default=True,verbose_name='Fecha asignado')
    fecha_proceso = models.DateTimeField(default=True,verbose_name='Fecha proceso')
    fecha_resuelto = models.DateTimeField(default=True,verbose_name='Fecha resuelto')
    fecha_validado = models.DateTimeField(default=True,verbose_name='Fecha validado')
    fecha_cancelado = models.DateTimeField(default=True,verbose_name='Fecha cancelado')
    ticket_superior = models.BigIntegerField()
    def __str__(self):
        return self.ticket_usariocreador
    def __str__(self):
        return self.ticket_especialistaasignado
    def __str__(self):
        return self.tipo_prioridad
    def __str__(self):
        return self.ticket_tipostatus
    def __str__(self):
        return self.ticket_proyecto
    def __str__(self):
        return self.ticket_areaorigen

# Clase para la tabla Comentario
class comentario(models.Model):
    comentario_usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE, related_name='comentario')
    fecha_comentario = models.DateTimeField(default=timezone.now)
    comentario_ticket = models.ForeignKey(ticket, null=True, blank=True, on_delete=models.CASCADE)
    contenido_ticket = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField()

# Clase para la tabla del Historial del Ticket
class historial_ticket(models.Model):
    ht_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    ht_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha modificacion')
    status_anterior = models.ForeignKey(status_ticket, null=True, blank=True, on_delete=models.CASCADE)


