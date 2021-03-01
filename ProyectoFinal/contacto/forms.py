from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre",required=True,max_length=50)
    email = forms.CharField(label="Email",required=True,max_length=60)
    contenido = forms.CharField(label="Contenido",required=False,max_length=1000,widget=forms.Textarea)


