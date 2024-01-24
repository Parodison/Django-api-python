from django.db import models

# Create your models here.

class Gestion(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefono = models.IntegerField()
    cedula = models.IntegerField()
    password = models.CharField(max_length=200)