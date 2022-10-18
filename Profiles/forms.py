from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil

class SignUpForm(UserCreationForm):
    Nombre = forms.CharField(max_length=140, required=True)
    Apellidos = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'Nombre',
            'Apellidos',
            'password1',
            'password2',
        )
