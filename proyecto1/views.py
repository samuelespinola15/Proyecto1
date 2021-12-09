from django.http import HttpResponse
import datetime

def saludo(request): #primera vista


	return HttpResponse("Hola amigos")


def dameFecha(request):
	fecha_actual=datetime.datetime.now()
	return HttpResponse("La fecha y hora actual es: %s"%fecha_actual)

def calculaEdad(request,edad,anio):
	#edadActual=18
	periodo=anio-2021
	edadFutura=edad+periodo
	return HttpResponse("En el año %s tendras %s años xd" %(anio,edadFutura))