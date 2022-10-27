from django import forms
from .models import Comentario


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido_ticket',)
        widgets = {

            'contenido_ticket': forms.Textarea(attrs={'class': 'form-control'}),
        }
