from django.db import models

# Create your models here.

class Vehiculos(models.Model):
	ARRAY_TIPO = (
		("Motocicleta","Motocicleta"),
		("Automovil","Automovil"),
		("Monopatin","Monopatin")
		)

	tipo = models.CharField(max_length=11, blank=False ,choices=ARRAY_TIPO)
	marca = models.CharField(max_length=50, blank=False)
	modelo =models.CharField(max_length=50, blank=False)

	def __str__(self):
		return self.modelo
