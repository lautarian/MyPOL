
from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

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

def login2(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "login2.html", {'form': form})