from django.db import models
from .choices import status_entidades
from .choices import roles
from .choices import prioridades
from .choices import status_tickets
from django.utils import timezone
from django.urls import reverse


# Clase Status entidad
class Status_E(models.Model):

    tipo_estatus = models.CharField(max_length=50, choices=status_entidades, default='ACTIVO')
    #AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha incial')
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_estatus


# Clase Proyecto
class Proyecto(models.Model):

    nombre_proyecto = models.CharField(max_length=150)
    codigo_proyecto = models.CharField(max_length=10, unique=True)

    fecha_inicial = models.DateTimeField(auto_now_add=True, verbose_name='Fecha incial')
    fecha_final = models.DateTimeField(null=True, verbose_name='Fecha final del proyecto')

    descripcion = models.TextField(null=True, blank=True)

    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status_entidad = models.ForeignKey(Status_E,
                                       null=True, blank=True,
                                       on_delete=models.CASCADE)

    # AUDITORIA
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre_proyecto


# Clase Area
class Area(models.Model):
    nombre_area = models.CharField(max_length=150)
    codigo_area = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    area_proyecto = models.ForeignKey(Proyecto, null=True, blank=True,
                                            on_delete=models.CASCADE)
    status_entidad = models.ForeignKey(Status_E,
                                       null=True, blank=True,
                                       on_delete=models.CASCADE)
    # AUDITORIA
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre_area


# Clase Rol para la tabla Usuario
class Rol(models.Model):

    tipo_rol = models.CharField(max_length=2, choices=roles, default='SA')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)


    def __str__(self):
        return self.tipo_rol


# Clase Especilidad para la tabla Especialista
class Especialidad(models.Model):

    tipo_especialidad = models.CharField(max_length=100)
    proyecto_especialidad = models.ForeignKey(Proyecto,
                                              null=True, blank=True,
                                              on_delete=models.CASCADE)
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_especialidad


# Clase Usuario
class Usuario(models.Model):
    codigo_usuario = models.CharField(max_length=20, unique=True)

    nombre_usuario = models.TextField(max_length=150, verbose_name='Nombre usuario')
    apellidos_usuario = models.TextField(max_length=250, verbose_name='Apellidos')
    email_usuario = models.EmailField(unique=True, verbose_name='Correo electrónico')
    password = models.CharField(max_length=8, verbose_name='Contraseña')
    usuario_rol = models.ForeignKey(Rol,
                                    null=True, blank=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Rol')

    usuario_proyecto = models.ManyToManyField(Proyecto, verbose_name='Proyecto')
    usuario_area = models.ManyToManyField(Area, verbose_name='Área')

    status_entidad = models.ForeignKey(Status_E, null=True, blank=True, on_delete=models.CASCADE)

    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # import pdb; pdb.set_trace()
        return str(self.nombre_usuario) + " " + str(self.apellidos_usuario)


# Clase Especialista para la tabla Especilidad
class Especialista(models.Model):

    status_entidad = models.ForeignKey(Status_E,
                                       null=True, blank=True,
                                       on_delete=models.DO_NOTHING)
    especialista_especialidad = models.ManyToManyField(Especialidad)
    especialista_usuario = models.ForeignKey(Usuario, verbose_name='especialista_u', on_delete=models.CASCADE,
                                             null=True, db_column='especialista_usuario')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        # import pdb; pdb.set_trace()
        return str(self.especialista_usuario)

    class Meta:
        db_table = '"HelpdeskApp_Especialista"'


# Clase para la tabla Prioridad
class Prioridad(models.Model):

    tipo_prioridad = models.CharField(max_length=50, choices=prioridades, default='Urgente')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_prioridad


# Clase para la tabla que relaciona el Estatus y Ticket
class Status_Ticket(models.Model):

    tipo_estatus = models.CharField(max_length=10, choices=status_tickets, default='Creado')
    # AUDITORIA
    fecha_creacion = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.tipo_estatus


# Clase para la tabla del Ticket
# Post
class Ticket(models.Model):
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
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True)
    # fecha de creacion
    publish = models.DateTimeField(default=timezone.now, verbose_name='Fecha creacion')
    # author
    ticket_usario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Usuario')
    ticket_especialista = models.ForeignKey(Especialista, null=True, blank=True, on_delete=models.CASCADE,
                                            verbose_name='Especialista')
    ticket_tipoprioridad = models.ForeignKey(Prioridad, null=True, blank=True, on_delete=models.CASCADE,
                                             verbose_name='Prioridad')
    # tipo status (9 status)
    ticket_tipostatus = models.ForeignKey(Status_Ticket, null=True, blank=True, on_delete=models.CASCADE,
                                          verbose_name='Status')
    # status
    status = models.CharField(max_length=10, choices=options, default='draft', verbose_name='Activo/Inactivo')
    coordenadas = models.CharField(max_length=30)
    evidencias = models.FileField(upload_to='evidencias', max_length=250, null=True, blank=True)
    # content
    descripcion = models.TextField(null=True)
    ticket_proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE,
                                        verbose_name='Proyecto')
    ticket_areaorigen = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Área')

    comentario_t = models.TextField(verbose_name='Comentario')

    # fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
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

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.titulo


# Clse Evidencias de ticket
class Evidencia_Ticket(models.Model):
    evidencia = models.BinaryField()

    evidencia_ticket = models.ManyToManyField(Ticket)


# Clase para la tabla Comentario
# Comment
class Comentario(models.Model):
    # name, email

    comentario_usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE,
                                           related_name='comments')
    # publish
    fecha_comentario = models.DateTimeField(default=timezone.now)
    # post
    comentario_ticket = models.ForeignKey(Ticket, null=True, blank=True, on_delete=models.CASCADE)
    # content
    contenido_ticket = models.TextField()

    fecha_creacion = models.DateTimeField(default=timezone.now, null=True, blank=True)
    fecha_culminacion = models.DateTimeField(null=True)

    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-fecha_comentario',)

    def __str__(self):
        return f'Comment by {self.comentario_usuario}'




