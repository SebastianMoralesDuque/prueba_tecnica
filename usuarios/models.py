from django.contrib.auth.models import User
from django.db import models
from localizaciones.models import Comuna


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_lider = models.BooleanField(default=False)


class Lider(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    superusuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lideres_asignados')
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    foto_perfil = models.CharField(max_length=255)


class Capitan(models.Model):
    id_capitan = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
