from django.urls import path
from . import views

urlpatterns = [

path("",views.inicio,name="inicio"),
path("editar/",views.editar,name="editar"),
path("eliminar/<int:vehiculo_id>",views.eliminar, name="eliminar"),
path("añadir/",views.añadir, name="añadir"),




]