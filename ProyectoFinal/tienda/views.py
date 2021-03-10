from django.shortcuts import render
from .models import Producto
# Create your views here.

def tienda(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista Tienda :

    """

    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html',{"productos":productos})