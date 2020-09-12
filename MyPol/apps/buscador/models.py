from django.db import models
from django.http import HttpResponse
# Create your models here.


class sqlserverconn(models.Model):
    nombrePrestador=models.CharField(max_length=500)
    nombreEspecialidad=models.CharField(max_length=200)
    direccionPrestador= models.CharField(max_length=500)
    telefonoPrestador=models.CharField(max_length=20)
    localidadPrestador=models.CharField(max_length=50)
    provinciaPrestador= models.CharField(max_length=50)
    
class Localidad(models.Model):
    idLocalidad=models.IntegerField()
    nombreLocalidad=models.CharField(max_length=50)
    
class Especialidad(models.Model):
    idEspecialidad=models.IntegerField()
    nombreEspecialidad=models.CharField(max_length=200)