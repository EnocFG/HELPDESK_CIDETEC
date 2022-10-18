from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=False)

    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):  
    try:
        instance.perfil.save()
    except ObjectDoesNotExist:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()