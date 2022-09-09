from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse

from .constants import ARRAY_TIPO
from .models import Vehiculos

# Create your views here.


def inicio(request):
	listaVehiculos = Vehiculos.objects.all()

	context = {'listaVehiculos' : listaVehiculos}

	return render(request, 'crud/inicio.html', context);


#########################################################################

#Tengo un tema con las urls.py y las def , que seguramente tengo definidas cosas de más, ya que por ejemplo: 

#La def "editar" la uso solamente para acceder al template editar.html que se encuentra en la url editar/ ; 


def editar(request):
		listaVehiculos = Vehiculos.objects.all()
		context = {'listaVehiculos' : listaVehiculos,
					'vehiculoAEditar' : None
					}
		return render(request, 'crud/editar.html',context);


#La def "editar_form" la uso para que me lleve a la url editar/vehiculo_id y cambia un poco el template editar.html con un condicional if;

def editar_form(request,vehiculo_id):
	listaVehiculos = Vehiculos.objects.all()

	vehiculoAEditar = Vehiculos.objects.get(pk=vehiculo_id)

	##filter => [1].marca
	## get => 1.marca
	
	print(vehiculoAEditar) #ésto no le des bola, era para ver si hacia algo la definicion.

	context = {'listaVehiculos': listaVehiculos,
				'vehiculoAEditar' : vehiculoAEditar  #esto lo uso en editar.html para usar el condicional if.
	}
	return render(request, 'crud/editar.html',context);

#La def "guardar_cambios" la usaría teoricamente para guardar los cambios, pero no pude ponerlo todo junto en "editar_form"
#porque la definicion anterior yo la uso para que me lleve recien a editar/vehiculo_id y no para editar todavia los cambios en si.

def guardar_cambios(request):
	vehiculo_id = request.POST.get('id')
	vehiculo_tipo = request.POST.get('Tipo')
	vehiculo_marca = request.POST.get('Marca')
	vehiculo_modelo = request.POST.get('Modelo')
	vehiculoAEditar = Vehiculos.objects.get(id=vehiculo_id)
	vehiculoAEditar.tipo = vehiculo_tipo
	vehiculoAEditar.marca = vehiculo_marca
	vehiculoAEditar.modelo = vehiculo_modelo
	vehiculoAEditar.save()

########################################################################################


def eliminar(request,vehiculo_id):
	listaVehiculos = Vehiculos.objects.all()

	vehiculoAEliminar = listaVehiculos.filter(id=vehiculo_id)
	vehiculoAEliminar.delete()
	return redirect('inicio');


#########################################################################################


def añadir_form(request):
	return render(request, 'crud/añadir.html')

def añadir(request):
	if request.method == "POST":
		print(request.POST.get('Tipo'))
		print(request.POST.get('Marca'))
		print(request.POST.get('Modelo'))
		tipo_añadir = request.POST.get('Tipo')
		marca_añadir = request.POST.get('Marca')
		modelo_añadir = request.POST.get('Modelo')
		vehiculoNuevo = Vehiculos(tipo=tipo_añadir,marca=marca_añadir,modelo=modelo_añadir)
		vehiculoNuevo.save()
		return inicio(request)
	if request.method == "GET":
		context = {

			"ARRAY_TIPO": ARRAY_TIPO
		}
		return render(request, 'crud/añadir.html', context)


#########################################################################################
