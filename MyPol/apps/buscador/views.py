from django.shortcuts import render
from django.http import HttpResponse
from .models import sqlserverconn
from .models import Localidad
from .models import Especialidad

from django.db import connection

# Create your views here.

def connsql(request):
    """ conn=pyodbc.connect('Driver={sql server};'
                        'Server=mypol.database.windows.net;'
                        'Database=MyPol;'
                        'UID=Administrador;'
                        'PWD=Info+2020') """
    cursor=connection.cursor()
    cursor.execute("SELECT [nombrePrestador], Esp.nombreEspecialidad, dir.direccion, "
    " Tel.prestadorTelefono, Loc.nombreLocalidad, Prov.nombreProvincia "
    "  FROM [dbo].[Prestador] Pres "
    " LEFT JOIN dbo.Especialidad Esp "
    " on Esp.id_especialidad=Pres.id_especialidad "
    " LEFT JOIN dbo.Direccion Dir "
    " on Dir.id_prestador=Pres.id_prestador "
    " LEFT JOIN dbo.TelefonoPrestador Tel "
    " on tel.id_prestador=pres.id_prestador "
    " LEFT JOIN dbo.Provincia Prov  "
    " on Prov.id_provincia = Dir.id_provincia "
    " LEFT JOIN  dbo.Localidad Loc "
    " on Loc.id_localidad = Dir.id_localidad ")
    

    result=cursor.fetchall()
    """return render(request,'index.html',{'sqlserverconn':result}) """

    # Cargo Localidades
    cursor2=connection.cursor()
    cursor2.execute("SELECT DISTINCT TOP (100) PERCENT id, nombreLocalidad AS NLoca "
                    "FROM            dbo.buscador_Localidad order by nombrelocalidad")    
    result2=cursor2.fetchall()
    
    # Cargo Especialidades
    cursor3=connection.cursor()
    cursor3.execute("SELECT DISTINCT TOP (100) PERCENT id, nombreEspecialidad AS NEspe "
                    "FROM            dbo.buscador_Especialidad order by nombreEspecialidad")    
    result3=cursor3.fetchall()
    
    
    
    return render(request,'encontraTuPol.html',{'sqlserverconn':result, 'Localidad':result2, 'Especialidad':result3})