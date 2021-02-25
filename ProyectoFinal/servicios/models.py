from django.db import models

#Creacion demodelos para el mapeo ORM

class Servicio(models.Model):
    """
    Este modelo representa una base de datos SQL
    donde cada variable representa una columna nueva en la B.D
    """
    titulo=models.CharField(max_length=50)

    contenido=models.CharField(max_length=50)

    imagen=models.ImageField(upload_to='servicios')

    created=models.DateTimeField(auto_now_add=True)

    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):

        return  self.titulo
