from django.urls import path
from . import views


# lista que contiene las URL´s creadas , las cuales se conectan con las vistas
# prueba
urlpatterns = [

    path('',views.blog,name="Blog"),
    path('categoria/<int:categoria_id>',views.categoria, name="categoria"),

]