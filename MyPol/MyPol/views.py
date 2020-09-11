
from django.shortcuts import render
import datetime

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {})

def registrate(request):
    return render(request, "registrate.html", {})

def recuperar(request):
    return render(request, "recuperar.html", {})

def encontraTuPol(request):
    return render(request, "encontraTuPol.html", {})

def resultadosBusq(request):
    return render(request, "resultadosBusq.html", {})

def perfilPOL(request):
    return render(request, "perfilPOL.html", {})

def miLista(request):
    return render(request, "miLista.html", {})