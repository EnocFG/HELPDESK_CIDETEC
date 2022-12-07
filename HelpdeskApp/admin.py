from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from django.contrib.admin.views.main import ChangeList

from django.contrib import admin
from django.contrib.gis import admin
from . import models
from .models import Status_E, Proyecto, Area, Rol,Especialidad, Usuario
from .models import Especialista, Prioridad, Status_Ticket, Evidencia_Ticket
from .models import Comentario, Ticket

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('folio', 'titulo', 'status')

admin.site.register(models.Ticket,AuthorAdmin)
admin.site.register(Status_E)
admin.site.register (Proyecto)
admin.site.register (Area)
admin.site.register (Rol)
admin.site.register (Especialidad)
admin.site.register (Usuario)
admin.site.register (Prioridad)
admin.site.register(Status_Ticket)
admin.site.register(Evidencia_Ticket)
admin.site.register(Comentario)
admin.site.register(Especialista)
# class EdificioAdmion(admin.OSMGeoAdmin):
#     pass







# class EspecialistaForm(ModelForm):
#     title = 'usuarios'
#     usuarios = forms.ModelMultipleChoiceField(
#         widget = FilteredSelectMultiple("especialista_usuario", is_stacked=False),
#         queryset = usuario.objects.all()
#     )
#     class Meta:
#         model = especialista
#         fields = ('usuarios',)
#
# @admin.register(especialista)
# class EspecialistaCatalogo(admin.ModelAdmin):
#     form = EspecialistaForm



