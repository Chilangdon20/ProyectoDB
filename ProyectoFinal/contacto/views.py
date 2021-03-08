from django.shortcuts import render,redirect
from .forms import  FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.
def contacto(request):
    """

    :param request:
    :return Solicitud render de URL ,acceso a la vista contacto :

    """
    formulario_contacto=FormularioContacto()

    """
    rescatar y validar la informacion del usuario , en caso
    de que todos los campos esten llenos.
    
    
    """
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde APP django",
                                 "El usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
                                 "",["chilangdonvazquez@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, 'contacto/contacto.html',{'miFormulario':formulario_contacto})