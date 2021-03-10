"""
Archivo encargado de comunicar las url de esta aplicaccion,
al proyecto principal , esto mediante la libreria urls
"""
# librerias a utilizar
from django.urls import path
from ProyectoWebApp import views
from . import views

# lista que contiene las URL´s creadas , las cuales se conectan con las vistas
urlpatterns = [


    path('',views.contacto,name='Contacto'),
]
