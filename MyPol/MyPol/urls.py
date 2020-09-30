"""MyPol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.buscador import views
from  django.views.generic.base  import  TemplateView 
from MyPol import views

from MyPol.forms import LoginForm

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name="login"),
    path('admin/', admin.site.urls),
    path('recuperar/',views.recuperar, name='recuperar'),
    path('encontraTuPol/',views.encontraTuPol, name='encontraTuPol'),
    path('resultadosBusq/',views.resultadosBusq, name='resultadosBusq'),
    path('<int:id>/',views.perfilPOL, name='perfilPOL'),
    path('miLista/',views.miLista, name='miLista'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('base/',views.base, name='base'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('logout/',views.logout_view, name="logout"),
 ]
