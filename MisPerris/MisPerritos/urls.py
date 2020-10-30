from django.contrib import admin
from django.urls import path, include
from .views import index,vision,registro,usuario,galeria,direccion,login,logout_view,admin_insumo,delete_insumo,modify_insumo,update

urlpatterns = [
    path('',index,name='INDEX'),
    path('vision/',vision,name='VISION'),
    path('registro/',registro,name='REGISTRO'),
    path('registro/usuario',usuario,name='USUARIO'),
    path('galeria/',galeria,name='GALERIA'),
    path('direccion/',direccion,name='DIRECCION'),
    path('login/',login,name='LOGIN'),
    path("logout/",logout_view,name="LOGOUT"),
    path("admin_insumos/",admin_insumo,name="ADMINI"),
    path("delete_insumo/<id>", delete_insumo, name="DELETEI"),
    path("modify_insumo/<name>", modify_insumo, name="MODIFYI"),
    path("update/", update, name="UPDATEI")
]