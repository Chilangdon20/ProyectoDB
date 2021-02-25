from django.shortcuts import render
from servicios.models import Servicio
# Create your views here.
def servicios(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista de servicios :

    """
    # importamos todos los servicios construidos
    servicios=Servicio.objects.all()

    return render(request, 'servicios/servicios.html', {'servicios':servicios})