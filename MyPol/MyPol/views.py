
from os import name
from django.shortcuts import render
import datetime
from django.shortcuts import render, render_to_response, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Template
from apps.buscador.models import  Localidad, Especialidad, sqlserverconn
import pyodbc
from .forms import InputForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
favoritos=[]

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

@login_required
def encontraTuPol(request):

    # Cargo Localidades
    localidad = Localidad.objects.all()
    especialidad=Especialidad.objects.all()
    context={
        'localidad':localidad,
        'especialidad':especialidad
    }    
    
    return render(request,'encontraTuPol.html',context)



@login_required
def resultadosBusq(request, id, espe):
    print('esto es id:'+id)
    if espe=="TODAS" and id=="TODAS":
        resultados= sqlserverconn.objects.all()
    elif id=="TODAS":
        resultados= sqlserverconn.objects.filter(nombreEspecialidad=espe)
    elif espe=="TODAS":
        resultados= sqlserverconn.objects.filter(localidadPrestador=id)
    else:
        resultados= sqlserverconn.objects.filter(localidadPrestador=id,nombreEspecialidad=espe)
    

    paginator = Paginator(resultados, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        prest = paginator.page(page)
    except PageNotAnInteger:
        prest = paginator.page(1)
    except EmptyPage:
        prest = paginator.page(paginator.num_pages)
        
    context={
        'page_obj':page_obj
    }

    return render(request,'resultadosBusq.html',context)


@login_required
def perfilPOL(request, id):
    resultados=sqlserverconn.objects.get(id= id)
    context={
        'resultados':resultados
    }
    #return render(request, 'project_detail.html',context)
    return render(request, "perfilPOL.html", context)

@login_required
def miLista(request):
    context={'favoritos':favoritos}
    
    return render(request, "miLista.html", context)


@login_required
def addFav(request, id):
    lista=sqlserverconn.objects.all()
    resultados=sqlserverconn.objects.get(id= id)

    if resultados not in favoritos:
        favoritos.append(resultados)
        
    context={'resultados':resultados,
                'lista':lista,
                'favoritos':favoritos}
    return render(request,'miLista.html',context)

def base(request):
    return render(request, "base.html")


def logout_view(request):
    logout(request)
    return redirect('login')

def miperfil(request):
    return render(request, "perfil.html")