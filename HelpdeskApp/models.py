from django.db import models


# Create your models here.
class proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=40)
    codigo_proyecto = models.CharField(max_length=5)
    fecha_inicio = models.DateTimeField(verbose_name='Fecha inicio')
    fecha_culminacion = models.DateTimeField(verbose_name='Fecha culminacion')
    descripcion = models.BigIntegerField()

    def __str__(self):
        return self.nombre_proyecto


class rol(models.Model):
    tipo_rol = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo_rol

class especialidad(models.Model):
    tipo_especialidad = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo_especialidad

class status(models.Model):
    tipo_status = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo_status

class prioridad(models.Model):
    tipo_prioridad = models.CharField(max_length=40)
    def __str__(self):
        return self.tipo_prioridad


class area(models.Model):
    nombre_area = models.CharField(max_length=40)
    codigo_area = models.CharField(max_length=5)
    id_proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_area

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=40)
    apellidos_usuario = models.CharField(max_length=40)
    email_usuario = models.EmailField()
    password_usuario = models.CharField(max_length=40)
    rol_usuario = models.ForeignKey(rol, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(especialidad, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    area = models.ForeignKey(area, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_usuario + " " +self.apellidos_usuario
    class Meta:
        ordering = ['id']

class especialista(models.Model):
    tipo_especialidad = models.ForeignKey(especialidad, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)



class problemas(models.Model):
    tipo_problemas = models.CharField(max_length=40)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creacion')
    fecha_culminacion = models.DateTimeField(verbose_name='Fecha culminacion')
    def __str__(self):
        return self.tipo_problemas

class ticket(models.Model):
    folio = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    especialista = models.ForeignKey(especialista, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(prioridad, on_delete=models.CASCADE)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    coordenandas = models.CharField(max_length=40)
    evidencia = models.ImageField()
    descripcion = models.BigIntegerField()
    problemas = models.ForeignKey(problemas, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creacion')
    fecha_atendido = models.DateTimeField(verbose_name='Fecha atendido')
    fecha_asignado = models.DateTimeField(verbose_name='Fecha asignado')
    fecha_proceso = models.DateTimeField(verbose_name='Fecha proceso')
    fecha_espera = models.DateTimeField(verbose_name='Fecha espera')
    fecha_resuelto = models.DateTimeField(verbose_name='Fecha resuelto')
    fecha_validado = models.DateTimeField(verbose_name='Fecha validado')
    fecha_cancelado = models.DateTimeField(verbose_name='Fecha cancelado')
    comentario = models.BigIntegerField()

# class comentario(models.Model):
#     descripcion_ticket = models.CharField(max_length=40)
#     id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
#     id_ticket_fk = models.ForeignKey(ticket, on_delete=models.CASCADE)


class historial_ticket(models.Model):
    id_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha modificacion')
    id_status_anterior = models.ForeignKey(status, on_delete=models.CASCADE)
    id_especialidad_anterior = models.ForeignKey(especialidad, on_delete=models.CASCADE)


# class ticket_relacionales(models.Model):
#     id_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
#     id_ticketn = models.ForeignKey(ticket, on_delete=models.CASCADE)
#     fecha_creacion = models.DateTimeField(verbose_name='Fecha creacion')
