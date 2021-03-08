from django.shortcuts import render

# Create your views here.

def tienda(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista Tienda :

    """
    return render(request, 'tienda/tienda.html')