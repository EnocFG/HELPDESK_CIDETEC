from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from django.contrib.admin.views.main import ChangeList


from .models import Status_E
from .models import Proyecto
from .models import Area
from .models import Rol
from .models import Especialidad
from .models import Usuario
from .models import Especialista
from .models import Prioridad
from .models import Status_Ticket
from .models import Evidencia_Ticket
from .models import Comentario
from . import models
from .models import ejemplo


from .models import Ticket




# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('folio', 'titulo', 'status')

admin.site.register(models.Ticket,AuthorAdmin)


admin.site.register(Status_E)
admin.site.register (Proyecto,)
admin.site.register (Area,)
admin.site.register (Rol,)
admin.site.register (Especialidad,)
admin.site.register (Usuario,)
admin.site.register (Prioridad,)
admin.site.register(Status_Ticket,)
admin.site.register(Evidencia_Ticket,)
admin.site.register(Comentario,)
admin.site.register(Especialista)
admin.site.register(ejemplo)




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



