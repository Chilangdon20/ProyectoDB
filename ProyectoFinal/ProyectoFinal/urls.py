"""
Configuración de URL de ProyectoFinal

La lista `urlpatterns` enruta las URL a las vistas. Para obtener más información, consulte:
     https://docs.djangoproject.com/en/2.2/topics/http/urls/
Ejemplos:
Vistas de funciones
     1. Agregar una importación: desde vistas de importación my_app
     2. Agregue una URL a urlpatterns: ruta ('', views.home, name = 'home')
Vistas basadas en clases
     1. Agregar una importación: de other_app.views import Home
     2. Agregue una URL a urlpatterns: ruta ('', Home.as_view (), name = 'home')
Incluyendo otra URLconf
     1. Importe la función include (): desde django.urls import include, path
     2. Agregue una URL a urlpatterns: ruta ('blog /', include ('blog.urls'))
"""

# seccion de librerias y archivos a utilizar
from django.contrib import admin
from django.urls import path, include

# lista que contiene las URL´s creadas , las cuales se conectan con las vistas
urlpatterns = [

    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')),
    path('blog/', include('blog.urls')),
    path('contacto/', include('contacto.urls')),
    path('', include('ProyectoWebApp.urls')),
]
