from django.contrib import admin
from mypol.MyPol.apps.buscador.models import Especialidad


class EspecialidadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Especialidad,EspecialidadAdmin)