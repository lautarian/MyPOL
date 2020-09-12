from django.db import models

# Create your models here.


class sqlserverconn(models.Model):
    nombrePrestador=models.CharField(max_length=500)
    nombreEspecialidad=models.CharField(max_length=200)
    direccionPrestador= models.CharField(max_length=200)
    telefonoPrestador=models.CharField(max_length=20)
    localidadPrestador=models.CharField(max_length=30)
    provinciaPrestador= models.CharField(max_length=30)
    
    