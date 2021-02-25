from django.urls import path
from . import views


# lista que contiene las URL´s creadas , las cuales se conectan con las vistas
urlpatterns = [

    path('',views.blog,name="Blog"),
    path('categoria/<categoria_id>'),

]