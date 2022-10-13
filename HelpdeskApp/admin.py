from django.contrib import admin

from HelpdeskApp.models import status_e
from HelpdeskApp.models import proyecto
from HelpdeskApp.models import area
from HelpdeskApp.models import rol
from HelpdeskApp.models import especialidad
from HelpdeskApp.models import usuario
from HelpdeskApp.models import especialista
from HelpdeskApp.models import prioridad
from HelpdeskApp.models import status_ticket
from HelpdeskApp.models import ticket
from HelpdeskApp.models import comentario
from HelpdeskApp.models import historial_ticket





# Register your models here.
admin.site.register(status_e )
admin.site.register(proyecto)
admin.site.register(area)
admin.site.register(rol)
admin.site.register(especialidad)
admin.site.register(usuario)
admin.site.register(especialista)
admin.site.register(prioridad)
admin.site.register(status_ticket)
admin.site.register(ticket)
admin.site.register(comentario)
admin.site.register(historial_ticket)



