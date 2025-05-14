from django.contrib.auth.models import AbstractUser
from django.db import models

class Cuenta(AbstractUser):
    correo = models.EmailField(unique=True)

class Usuario(models.Model):
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)

            
