
from django.shortcuts import render
import datetime
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect

from apps.buscador.models import  Localidad, Especialidad, sqlserverconn

import pyodbc
from .forms import InputForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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
def resultadosBusq(request):
    resultados= sqlserverconn.objects.all()
    contexto2={
        'resultados':resultados
    }    

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
    #return render(request, "resultadosBusq.html", {})

@login_required
def perfilPOL(request):
    return render(request, "perfilPOL.html", {})

@login_required
def miLista(request):
    return render(request, "miLista.html", {})


def base(request):
    return render(request, "base.html")


def logout_view(request):
    logout(request)
    return redirect('login')


