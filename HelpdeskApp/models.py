from django.db import models
from django.urls import reverse
from django.utils import timezone
from .choices import prioridades
from .choices import roles
from .choices import estatus_entidades
from .choices import estatus_tickets
import pgtrigger
import pghistory


@pghistory.track(
    pghistory.AfterInsert(label="Inserción"),
    pghistory.BeforeUpdate(label="Antes de Actualizar"),
    pghistory.AfterUpdate(label="Actualización"),
    pghistory.BeforeDelete(label="Antes de Eliminar"),
)
class ejemplo(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    edad = models.IntegerField(null=True, verbose_name=("edad"))


# Clase estatus de las entidades
class estatus_e(models.Model):
    tipo_estatus = models.CharField(
        max_length=50, choices=estatus_entidades, default="Inactivo"
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha incial"
    )
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_estatus


# Clase Proyecto
class proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=150)
    codigo_proyecto = models.CharField(max_length=10)

    fecha_inicial = models.DateTimeField(null=True, verbose_name="Fecha incial")
    fecha_final = models.DateTimeField(
        null=True, verbose_name="Fecha final del proyecto"
    )

    descripcion = models.TextField(null=True, blank=True)

    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.CASCADE
    )

    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre_proyecto


# Clase Area
class area(models.Model):
    nombre_area = models.CharField(max_length=150)
    codigo_area = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    area_proyecto = models.ManyToManyField(proyecto)
    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.CASCADE
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    area_proyecto = models.ManyToManyField(proyecto)
    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.CASCADE
    )


# Clase Rol para la tabla Usuario
class rol(models.Model):
    tipo_rol = models.CharField(max_length=2, choices=roles, default="SA")
    # Auditoria
    fecha_creacion = models.DateTimeField(null=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_rol


# Clase Especilidad para la tabla Especialista
class especialidad(models.Model):
    tipo_especialidad = models.CharField(max_length=100)
    proyecto_especialidad = models.ForeignKey(
        proyecto, null=True, blank=True, on_delete=models.CASCADE
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_especialidad


# Clase Usuario
class usuario(models.Model):
    codigo_usuario = models.CharField(max_length=20, unique=True)

    nombre_usuario = models.TextField(max_length=150, verbose_name="Nombre usuario")
    apellidos_usuario = models.TextField(max_length=250, verbose_name="Apellidos")
    email_usuario = models.EmailField(unique=True, verbose_name="Correo electrónico")
    password = models.CharField(max_length=10, verbose_name="Contraseña")
    usuario_rol = models.ForeignKey(
        rol, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Rol"
    )

    usuario_proyecto = models.ManyToManyField(proyecto, verbose_name="Proyecto")
    usuario_area = models.ManyToManyField(area, verbose_name="Área")

    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.CASCADE
    )

    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.nombre_usuario) + " " + str(self.apellidos_usuario)

    class Meta:
        triggers = [
            pgtrigger.Protect(name="proteger_proyecto", operation=pgtrigger.Delete)
        ]


# Clase Especialista para la tabla Especilidad
class especialista(models.Model):
    estatus_entidad = models.ForeignKey(
        estatus_e, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    especialista_especialidad = models.ManyToManyField(especialidad)
    especialista_usuario = models.ForeignKey(
        usuario,
        verbose_name="especialista_u",
        on_delete=models.CASCADE,
        null=True,
        db_column="especialista_usuario",
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.especialista_usuario)

    class Meta:
        db_table = '"HelpdeskApp_Especialista"'


# Clase para la tabla Prioridad
class prioridad(models.Model):
    tipo_prioridad = models.CharField(
        max_length=50, choices=prioridades, default="Urgente"
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_culminacion = models.DateTimeField(null=True)

    def __str__(self):
        return self.tipo_prioridad


# Clase para la tabla que relaciona el Estatus y Ticket
class estatus_ticket(models.Model):
    tipo_estatus = models.CharField(
        max_length=10, choices=estatus_tickets, default="Creado"
    )
    # Auditoria
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo_estatus


# Clase para la tabla del Ticket
# Post
class ticket(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
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
    usario = models.ForeignKey(
        usuario, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Usuario"
    )
    especialista = models.ForeignKey(
        especialista,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Especialista",
    )
    prioridad = models.ForeignKey(
        prioridad,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Prioridad",
    )
    # tipo status (9 status)
    estatus = models.ForeignKey(
        estatus_ticket,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Status",
    )
    # status
    estatus_entidad = models.CharField(
        max_length=10, choices=options, default="draft", verbose_name="Activo/Inactivo"
    )
    coordenadas = models.CharField(null=True, max_length=30)
    evidencias = models.FileField(
        upload_to="evidencias", max_length=250, null=True, blank=True
    )
    # content
    descripcion = models.TextField(null=True)
    proyecto = models.ForeignKey(
        proyecto,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Proyecto",
    )
    area_origen = models.ForeignKey(
        area, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Área"
    )

    comentario_t = models.TextField(null=True, blank=True, verbose_name="Comentario")

    fecha_creacion = models.DateTimeField(auto_now=True, verbose_name="Fecha creacion")
    fecha_atendido = models.DateTimeField(null=True, verbose_name="Fecha atendido")
    fecha_asignado = models.DateTimeField(null=True, verbose_name="Fecha asignado")
    fecha_proceso = models.DateTimeField(null=True, verbose_name="Fecha proceso")
    fecha_resuelto = models.DateTimeField(null=True, verbose_name="Fecha resuelto")
    fecha_validado = models.DateTimeField(null=True, verbose_name="Fecha validado")
    fecha_cancelado = models.DateTimeField(null=True, verbose_name="Fecha cancelado")
    ticket_superior = models.BigIntegerField(null=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse("HelpdeskApp:ticket_single", args=[self.slug])

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
    comentario_usuario = models.ForeignKey(
        usuario,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    # publish
    fecha_comentario = models.DateTimeField(default=timezone.now)
    # post
    comentario_ticket = models.ForeignKey(
        ticket, null=True, blank=True, on_delete=models.CASCADE
    )
    # content
    contenido_ticket = models.TextField(null=True, blank=True)

    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("-fecha_comentario",)

    def __str__(self):
        return f"Comentado por {self.comentario_usuario}"
