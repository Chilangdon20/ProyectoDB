"""
Archivo encargado de comunicar las url de esta aplicaccion,
al proyecto principal , esto mediante la libreria urls
"""
# librerias a utilizar
from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

# lista que contiene las URL´s creadas , las cuales se conectan con las vistas
urlpatterns = [

    path('',views.home,name='Home'),


]
# especificamos la ruta para que se puedan mostrar nuestras imagenes

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)