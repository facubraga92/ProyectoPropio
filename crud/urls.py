from django.urls import path
from . import views

urlpatterns = [

path("",views.inicio,name="inicio"),


path("editar/<int:vehiculo_id>",views.editar_form,name="editar_form"),
path("editar/",views.editar, name="editar"),
path("guardar_cambios/",views.guardar_cambios, name="guardar_cambios"),


path("eliminar/<int:vehiculo_id>",views.eliminar, name="eliminar"),


path("añadir/",views.añadir, name="añadir"),
path("añadir_form/",views.añadir_form, name="añadir_form")





]