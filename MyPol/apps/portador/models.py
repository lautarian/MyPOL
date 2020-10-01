from django.db import models
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your models here.


class sqlserverconn(models.Model):
    id_prestador=models.IntegerField
    nombrePrestador=models.CharField(max_length=500)
    nombreEspecialidad=models.CharField(max_length=200)
    direccionPrestador= models.CharField(max_length=200)
    telefonoPrestador=models.CharField(max_length=20)
    localidadPrestador=models.CharField(max_length=30)
    provinciaPrestador= models.CharField(max_length=30)
    favourite= models.ManyToManyField(User, related_name="fav_prestador", blank=True)
    
class PrestList(ListView):
    paginate_by = 2
    model = sqlserverconn


    
