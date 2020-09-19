
from django.shortcuts import render
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from apps.buscador.models import sqlserverconn
from apps.buscador.models import Localidad
from apps.buscador.models import Especialidad
import pyodbc


def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {})

def registrate(request):
    return render(request, "registrate.html", {})

def recuperar(request):
    return render(request, "recuperar.html", {})

def encontraTuPol(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=tcp:mypol.database.windows.net;'
                        'Database=MyPol;'
                        'UID=Administrador;'
                        'PWD=Info+2020;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor=conn.cursor()
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
    cursor2=conn.cursor()
    cursor2.execute("SELECT DISTINCT TOP (100) PERCENT id_localidad, nombreLocalidad AS NLoca "
                    "FROM            dbo.Localidad order by nombrelocalidad")    
    result2=cursor2.fetchall()
    
    # Cargo Especialidades
    cursor3=conn.cursor()
    cursor3.execute("SELECT DISTINCT TOP (100) PERCENT id_especialidad, nombreEspecialidad AS NEspe "
                    "FROM            dbo.Especialidad order by nombreEspecialidad")    
    result3=cursor3.fetchall()
    
    
    
    return render(request,'encontraTuPol.html',{'sqlserverconn':result, 'Localidad':result2, 'Especialidad':result3})

def resultadosBusq(request):
    conn2=pyodbc.connect('Driver={sql server};'
                        'Server=tcp:mypol.database.windows.net;'
                        'Database=MyPol;'
                        'UID=Administrador;'
                        'PWD=Info+2020;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor2=conn2.cursor()
    cursor2.execute("SELECT [nombrePrestador], Esp.nombreEspecialidad, dir.direccion, "
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
    

    result=cursor2.fetchall()
    return render(request,'resultadosBusq.html',{'sqlserverconn':result})
    #return render(request, "resultadosBusq.html", {})

def perfilPOL(request):
    return render(request, "perfilPOL.html", {})

def miLista(request):
    return render(request, "miLista.html", {})


def base(request):
    return render(request, "base.html")



