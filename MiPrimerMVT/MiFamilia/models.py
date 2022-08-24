from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    fecha_de_nacimiento = models.DateField()
    dni = models.PositiveIntegerField()
    numero_de_telefono  = models.PositiveIntegerField()
    nacionalidad = models.CharField(max_length=10)
    parentesco  =  models.CharField(max_length=10)