from django.db import models


class status_entidad (models.Model):

    tipo_estatus = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()

class proyecto (models.Model):

    nombre_proyecto = models.CharField(max_length=10)
    codigo_proyecto = models.CharField(max_length=5)
    fecha_inicial = models.DateTimeField(verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(verbose_name='Fecha final')
    descripcion  = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
    status_entidad = models.ForeignKey(status_entidad , on_delete=models.CASCADE)

class area (models.Model):

    nombre_area = models.CharField(max_length=10)
    codigo_area = models.CharField(max_length=5)
    fecha_inicial = models.DateTimeField(verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(verbose_name='Fecha final')
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
    proyecto_area = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    status_entidad = models.ForeignKey(status_entidad , on_delete=models.CASCADE)

class rol (models.Model):

    tipo_rol= models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
class especalidad (models.Model):

    tipo_especialidad  = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
class area_usuario (models.Model):

    usuario= models.ForeignKey(usuario, on_delete=models.CASCADE)
    proyecto= models.ForeignKey(proyecto, on_delete=models.CASCADE)
    area= models.ForeignKey(area, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
class usuario (models.Model):

    codigo_usuario = models.CharField(max_length=5)
    nombre_usuario = models.CharField(max_length=30, verbose_name='Nombre del usuario')
    apellidos_usuario= models.CharField(max_length=30, verbose_name='Appellios del usuario')
    email_usuario= models.EmailField(verbose_name='Nombre del usuario')
    password = models.CharField(max_length=8)
    usuario_rol= models.ForeignKey(rol, on_delete=models.CASCADE)
    usuario_proyecto= models.ForeignKey(proyecto, on_delete=models.CASCADE)
    usuario_area= models.ForeignKey(area_usuario, on_delete=models.CASCADE)
    usuario_especialista= models.ForeignKey(especialista, on_delete=models.CASCADE)
    status_entidad = models.ForeignKey(status_entidad, on_delete=models.CASCADE)
class especialista (models.Model):

    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
    status_entidad = models.ForeignKey(status_entidad, on_delete=models.CASCADE)
    especialista_especialidad = models.ForeignKey(especalidad, on_delete=models.CASCADE)
    especialista_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class prioridad (models.Model):
    tipo_prioridad = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
class status_ticket (models.Model):

    tipo_estatus = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
class ticket (models.Model):

    folio = models.CharField(max_length=20)
    titulo = models.CharField(max_length=5)
    ticket_usariocreador = models.ForeignKey(usuario, on_delete=models.CASCADE)
    ticket_especialistaasignado = models.ForeignKey(especialista, on_delete=models.CASCADE)
    ticket_tipoprioridad = models.ForeignKey(prioridad, on_delete=models.CASCADE)
    ticket_tipostatus = models.ForeignKey(status_ticket, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=30)
    evidencias= models.ImageField()
    descripcion = models.CharField(max_length=100)
    ticket_proyecto = models.ForeignKey(proyecto, on_delete=models.CASCADE)
    ticket_areaorigen= models.ForeignKey(area, on_delete=models.CASCADE)
    ticket_areadestino = models.ForeignKey(area_usuario, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creacion')
    fecha_atendido = models.DateTimeField(verbose_name='Fecha atendido')
    fecha_asignado = models.DateTimeField(verbose_name='Fecha asignado')
    fecha_proceso = models.DateTimeField(verbose_name='Fecha proceso')
    fecha_espera = models.DateTimeField(verbose_name='Fecha espera')
    fecha_resuelto = models.DateTimeField(verbose_name='Fecha resuelto')
    fecha_validado = models.DateTimeField(verbose_name='Fecha validado')
    fecha_cancelado = models.DateTimeField(verbose_name='Fecha cancelado')
    ticket_superior = models.BigIntegerField()
class comentario(models.Model):
    descripcion_ticket = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField()
    fecha_culminacion = models.DateTimeField()
    comentario_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    comentario_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
class historial_ticket (models.Model):

    ht_ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    ht_usuario = models.ForeignKey(usuario, on_delete = models.CASCADE)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha modificacion')
    status_anterior = models.ForeignKey(status_ticket, on_delete=models.CASCADE)
    especialista_anterior = models.ForeignKey(especialista, on_delete=models.CASCADE)
