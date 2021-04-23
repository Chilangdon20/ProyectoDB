#Archivo encargado de administrar los utusaios de nuestra DB

from django.contrib import admin
from .models import Categoria,Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


# Registramos nuestras clases
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)
