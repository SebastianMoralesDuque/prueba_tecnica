from django.db import models
from localizaciones.models import PuestoVotacion, Barrio
from usuarios.models import Lider

class Votante(models.Model):
    id_votante = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    puesto_votacion = models.ForeignKey(PuestoVotacion, on_delete=models.CASCADE)
    lider = models.ForeignKey(Lider, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
