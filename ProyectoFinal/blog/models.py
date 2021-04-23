from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
Los modelos son las clases que definimos con las cuales
django interpreta como una base de datos, a la cual
le declaramos sus atributos.

"""

class Categoria(models.Model):
    """
    Atributos:

    nombre - Nombre del usuario.
    created - fehca en la cual se creo la categoria
    updated - Atributo encargado de generar la fecha de actualizacion de la
    categoria
    """
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    """

    Clas encargada de generar el modelo Post, este genera un post creado por el
    usuario
    Atributos:
    titluo- VARCHAR 50
    contenido - VARCHAR 50
    image - ImageField -NO es obligatorio.
    AUTOR - Clave secundaria, relacionada con el atributo User.
    categorias - Primary Key
    created - DATE Standard Format.
    updated - DATE Standard format.

    """
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="blog", null=True,blank=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE) # establecemos relacion entre usuario.
    categorias=models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo
