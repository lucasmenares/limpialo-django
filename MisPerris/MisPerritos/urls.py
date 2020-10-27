from django.contrib import admin
from django.urls import path, include
from .views import index,vision,registro,usuario,insumos,galeria,direccion

urlpatterns = [
    path('',index,name='INDEX'),
    path('vision/',vision,name='VISION'),
    path('registro/',registro,name='REGISTRO'),
    path('registro/usuario',usuario,name='USUARIO'),
    path('registro/insumos',insumos,name='INSUMOS'),
    path('galeria/',galeria,name='GALERIA'),
    path('direccion/',direccion,name='DIRECCION'),
]