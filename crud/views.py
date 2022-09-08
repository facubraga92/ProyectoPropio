from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Vehiculos
# Create your views here.



def inicio(request):
	listaVehiculos = Vehiculos.objects.all()
	context = {'listaVehiculos' : listaVehiculos}

	return render(request, 'crud/inicio.html', context);

def editar(request):
	listaVehiculos = Vehiculos.objects.all()
	context = {'listaVehiculos': listaVehiculos}
	return render(request, 'crud/editar.html',context);

def añadir(request):
	print(request.POST.get('Tipo'))
	print(request.POST.get('Marca'))
	print(request.POST.get('Modelo'))

	return render(request, 'crud/añadir.html')


def eliminar(request,vehiculo_id):
	listaVehiculos = Vehiculos.objects.all()
	vehiculoAEliminar = listaVehiculos.filter(id=vehiculo_id)
	vehiculoAEliminar.delete()
	listaVehiculos = Vehiculos.objects.all()
	context = {'listaVehiculos': Vehiculos.objects.all()}

	return render(request, 'crud/editar.html', context);


