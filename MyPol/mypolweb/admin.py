from django.contrib import admin
from mypol.MyPol.apps.buscador.models import Especialidad

# Register your models here.
class EspecialidadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Especialidad,EspecialidadAdmin)

