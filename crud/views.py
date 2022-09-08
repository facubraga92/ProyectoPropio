from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Vehiculos
# Create your views here.

listaVehiculos = Vehiculos.objects.all()

def inicio(request):
	context = {'listaVehiculos' : listaVehiculos}

	return render(request, 'crud/inicio.html', context);

def editar(request):
	context = {'listaVehiculos': listaVehiculos}
	return render(request, 'crud/editar.html',context);

def añadir(request):
	print(request.POST.get('Tipo'))
	print(request.POST.get('Marca'))
	print(request.POST.get('Modelo'))

	return render(request, 'crud/añadir.html')


def eliminar(request,vehiculo_id):
	vehiculoAEliminar = listaVehiculos.filter(id=vehiculo_id)
	vehiculoAEliminar.delete()
	return redirect('inicio');


