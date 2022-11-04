from django.db import models
from django.urls import reverse
from django.utils import timezone

<<<<<<< HEAD
=======
from .choices import roles
>>>>>>> parent of 4049b6c (cambios en la base de datos)
from .choices import prioridades
from .choices import roles
from .choices import status_entidades
from .choices import status_tickets


# Clase status de las entidades correpondenes a proyecto, area, usuario, especialista
class status_e(models.Model):
<<<<<<< HEAD
    tipo_estatus = models.CharField(
        max_length=50, choices=status_entidades, default='Inactivo')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha incial')
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_estatus
=======
    tipo_estatus = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField()

>>>>>>> parent of 4049b6c (cambios en la base de datos)


# Clase Proyecto
class proyecto(models.Model):
<<<<<<< HEAD
    nombre_proyecto = models.CharField(max_length=150)
    codigo_proyecto = models.CharField(max_length=10)

    fecha_inicial = models.DateTimeField(
        null=True, verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(
        null=True, verbose_name='Fecha final del proyecto')

    descripcion = models.TextField(null=True, blank=True)

    status_entidad = models.ForeignKey(status_e,
                                       null=True, blank=True,
                                       on_delete=models.CASCADE)

    # AUDITORIA
=======
    nombre_proyecto = models.CharField(max_length=50)
    codigo_proyecto = models.CharField(max_length=5)
    fecha_inicial = models.DateTimeField(verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(verbose_name='Fecha final')
    descripcion = models.TextField(null=True)
>>>>>>> parent of 4049b6c (cambios en la base de datos)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)

<<<<<<< HEAD
    def __str__(self):
        return self.nombre_proyecto


# Clase Area
class area(models.Model):
    nombre_area = models.CharField(max_length=150)
    codigo_area = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    area_proyecto = models.ManyToManyField(proyecto)
    status_entidad = models.ForeignKey(status_e,
                                       null=True, blank=True,
                                       on_delete=models.CASCADE)
    # AUDITORIA
=======

# Clase Area para la tabla Proyecto
class area(models.Model):
    nombre_area = models.CharField(max_length=10)
    codigo_area = models.CharField(max_length=5)
    descripcion = models.TextField(null=True)
>>>>>>> parent of 4049b6c (cambios en la base de datos)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    area_proyecto = models.ManyToManyField(proyecto)
    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)


# Clase Rol para la tabla Usuario


# Clase Rol para la tabla Usuario
class rol(models.Model):
    tipo_rol = models.CharField(max_length=2, choices=roles, default='SA')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(null=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_rol


# Clase Especilidad para la tabla Especialista
class especialidad(models.Model):
    tipo_especialidad = models.CharField(max_length=100)
    proyecto_especialidad = models.ForeignKey(proyecto,
                                              null=True, blank=True,
                                              on_delete=models.CASCADE)
    # AUDITORIA
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_especialidad


# Clase Usuario
class usuario(models.Model):
    codigo_usuario = models.CharField(max_length=20, unique=True)

    nombre_usuario = models.TextField(max_length=150, verbose_name='Nombre usuario')
    apellidos_usuario = models.TextField(max_length=250, verbose_name='Apellidos')
    email_usuario = models.EmailField(unique=True, verbose_name='Correo electrónico')
    password = models.CharField(max_length=10, verbose_name='Contraseña')
    usuario_rol = models.ForeignKey(rol,
                                    null=True, blank=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Rol')

    usuario_proyecto = models.ManyToManyField(proyecto, verbose_name='Proyecto')
    usuario_area = models.ManyToManyField(area, verbose_name='Área')

    status_entidad = models.ForeignKey(status_e, null=True, blank=True, on_delete=models.CASCADE)

    # AUDITORIA
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.nombre_usuario) + " " + str(self.apellidos_usuario)


# Clase Especialista para la tabla Especilidad
class especialista(models.Model):
    status_entidad = models.ForeignKey(status_e,
                                       null=True, blank=True,
                                       on_delete=models.DO_NOTHING)
    especialista_especialidad = models.ManyToManyField(especialidad)
    especialista_usuario = models.ForeignKey(usuario, verbose_name='especialista_u', on_delete=models.CASCADE,
                                             null=True, db_column='especialista_usuario')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.especialista_usuario)

    class Meta:
        db_table = '"HelpdeskApp_Especialista"'


# Clase para la tabla Prioridad
class prioridad(models.Model):
    tipo_prioridad = models.CharField(max_length=50, choices=prioridades, default='Urgente')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_prioridad


# Clase para la tabla que relaciona el Estatus y Ticket
class status_ticket(models.Model):
    tipo_estatus = models.CharField(max_length=10, choices=status_tickets, default='Creado')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo_estatus


# Clase para la tabla del Ticket
# Post
class ticket(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    folio = models.CharField(max_length=20, unique=True)
    # title
    titulo = models.CharField(max_length=250)
    # extracto
    # excerpt = models.TextField(null=True, verbose_name='Extracto')
    # slug = models.SlugField(null=True, max_length=250, unique_for_date='publish')
    # fecha de creacion
    # publish = models.DateTimeField(null=True, verbose_name='Fecha creacion')
    # author
    usario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Usuario')
    especialista = models.ForeignKey(especialista, null=True, blank=True, on_delete=models.CASCADE,
                                     verbose_name='Especialista')
    prioridad = models.ForeignKey(prioridad, null=True, blank=True, on_delete=models.CASCADE,
                                  verbose_name='Prioridad')
    # tipo status (9 status)
    ticket_tipostatus = models.ForeignKey(status_ticket, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name='Status')
    # status
    status = models.CharField(max_length=10, choices=options, default='draft', verbose_name='Activo/Inactivo')
    coordenadas = models.CharField(null=True, max_length=30)
    evidencias = models.FileField(upload_to='evidencias', max_length=250, null=True, blank=True)
    # content
    descripcion = models.TextField(null=True)
    proyecto = models.ForeignKey(proyecto, null=True, blank=True, on_delete=models.CASCADE,
                                 verbose_name='Proyecto')
    area_origen = models.ForeignKey(area, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Área')

    comentario_t = models.TextField(null=True, blank=True, verbose_name='Comentario')

    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name='Fecha creacion')
    fecha_atendido = models.DateTimeField(null=True, verbose_name='Fecha atendido')
    fecha_asignado = models.DateTimeField(null=True, verbose_name='Fecha asignado')
    fecha_proceso = models.DateTimeField(null=True, verbose_name='Fecha proceso')
    fecha_resuelto = models.DateTimeField(null=True, verbose_name='Fecha resuelto')
    fecha_validado = models.DateTimeField(null=True, verbose_name='Fecha validado')
    fecha_cancelado = models.DateTimeField(null=True, verbose_name='Fecha cancelado')
    ticket_superior = models.BigIntegerField(null=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse('HelpdeskApp:ticket_single', args=[self.slug])

    # class Meta:
    #     ordering = ('-publish',)

    def __str__(self):
        return self.titulo


# Clase Evidencias de ticket
class evidencia_ticket(models.Model):
    evidencia = models.BinaryField()
    evidencia_ticket = models.ManyToManyField(ticket)


# Clase para la tabla Comentario
class comentario(models.Model):
    comentario_usuario = models.ForeignKey(usuario, null=True, blank=True, on_delete=models.CASCADE,
                                           related_name='comments')
    # publish
    fecha_comentario = models.DateTimeField(default=timezone.now)
    # post
    comentario_ticket = models.ForeignKey(ticket, null=True, blank=True, on_delete=models.CASCADE)
    # content
    contenido_ticket = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-fecha_comentario',)

    def __str__(self):
        return f'Comentado por {self.comentario_usuario}'
