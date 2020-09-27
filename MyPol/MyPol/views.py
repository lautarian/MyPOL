
from django.shortcuts import render
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
""" from apps.buscador.models import sqlserverconn
from apps.buscador.models import Localidad
from apps.buscador.models import  Especialidad """
from apps.buscador.views import  *
import pyodbc
from .forms import InputForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection

def home(request):
    return render(request, "home.html", {})

def login(request):
    context={}
    context['form']=InputForm()
    return render(request, "login.html", context)

def registrate(request):
    return render(request, "registrate.html", {})

def recuperar(request):
    return render(request, "recuperar.html", {})

def encontraTuPol(request):
    """ conn=pyodbc.connect('Driver={sql server};'
                        'Server=tcp:mypol.database.windows.net;'
                        'Database=MyPol;'
                        'UID=Administrador;'
                        'PWD=Info+2020;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
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
    " on Loc.id_localidad = Dir.id_localidad ")"""
    

 #   result=cursor.fetchall()
#   return render(request,'index.html',{'sqlserverconn':result}) 

    # Cargo Localidades
    cursor2=connection.cursor()
    cursor2.execute("SELECT DISTINCT TOP (100) PERCENT id, nombreLocalidad AS NLoca "
                    "FROM            dbo.buscador_localidad order by nombrelocalidad")    
    result2=cursor2.fetchall()
    
    # Cargo Especialidades
    cursor3=connection.cursor()
    cursor3.execute("SELECT DISTINCT TOP (100) PERCENT  id, nombreEspecialidad AS NEspe "
                    "FROM            dbo.buscador_especialidad order by nombreEspecialidad")    
    result3=cursor3.fetchall()
    
    
    
    return render(request,'encontraTuPol.html',{'Localidad':result2, 'Especialidad':result3})

def resultadosBusq(request):
    parametro= request.GET.get("Fespe")
    print(parametro)
    cursor2=connection.cursor()
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
    " on Loc.id_localidad = Dir.id_localidad where Pres.id_especialidad =1")
    

    result=cursor2.fetchall()
    paginator = Paginator(result, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        prest = paginator.page(page)
    except PageNotAnInteger:
        prest = paginator.page(1)
    except EmptyPage:
        prest = paginator.page(paginator.num_pages)

    return render(request,'resultadosBusq.html',{'page_obj':page_obj,'sqlserverconn':prest})
    #return render(request, "resultadosBusq.html", {})

def perfilPOL(request):
    return render(request, "perfilPOL.html", {})

def miLista(request):
    return render(request, "miLista.html", {})


def base(request):
    return render(request, "base.html")


