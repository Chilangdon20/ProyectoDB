from django import forms

class FormularioContacto(forms.Form):
    """
    Clase encargada de generar un formulario el cual el cliente se puede poner

    en contacto con la empresa.

    Parametro: forms.form

    Variables creadas

    nombre - NOmbre del cliente .
    email - Email del cliente.
    contenido - MOtivo de contacto o razon por la cual mandar el correo.

    """
    nombre = forms.CharField(label="Nombre",required=True,max_length=50)
    email = forms.CharField(label="Email",required=True,max_length=60)
    contenido = forms.CharField(label="Contenido",required=False,max_length=1000,widget=forms.Textarea)
