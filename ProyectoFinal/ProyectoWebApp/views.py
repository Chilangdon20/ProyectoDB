# FERNANDO V.S
"""
Esta seccion de codgio consta de las vistas ,
estas son las encargadas de darle funcionalidad a nuestro proyecto,
las cuales se comunican por medio de URL´S con un parametro de funcion
llamado request, cada vista esta documentada con su funcion y sus parametros.
"""

# metodos y librerias a utilizar
from django.shortcuts import render,HttpResponse
# ruta especificada para importar una clase que se encuentra en el models de nuestra app Servicios
from servicios.models import Servicio
# Seccion de vistas

def home(request):
    """

    :param request:
    :return Solicitud HttpResponse de URL ,acceso al home :

    """
    return render(request,"ProyectoWebApp/home.html")





def tienda(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista Tienda :

    """
    return render(request,'ProyectoWebApp/tienda.html')








