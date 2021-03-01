from django.shortcuts import render
from .forms import  FormularioContacto
# Create your views here.
def contacto(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista contacto :

    """
    formulario_contacto  = FormularioContacto()
    return render(request, 'contacto/contacto.html',{'miFormulario':formulario_contacto})