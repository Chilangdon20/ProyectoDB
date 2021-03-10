from django.contrib import admin
from .models import Servicio

# Register your models here.
class SerivicioAdmin(admin.ModelAdmin):
    """
    Clase que incluya los campos que se
    rellenan automaticamente en el panel de administracion
    """
    readonly_fields = ('created','updated')

admin.site.register(Servicio,SerivicioAdmin)