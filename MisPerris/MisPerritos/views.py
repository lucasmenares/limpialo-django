from django.shortcuts import render
from .models import SliderPhoto,Mision,SliderGaleria,Usuario,Insumo

# Create your views here.
def index(request):
	autos = SliderPhoto.objects.all()
	return render(request,'web/index.html',{'autos':autos})

def vision(request):
	mision = Mision.objects.all()
	return render(request,'web/vision.html',{'mision':mision})

def registro(request):
	return render(request, 'web/registro/registro.html')

def usuario(request):
	return render(request, 'web/registro/usuario.html')

def insumos(request):
	return render(request, 'web/registro/insumos.html')

def galeria(request):
	autos = SliderGaleria.objects.all()
	#return render(request, 'web/galeria.html')
	return render(request,'web/galeria.html',{'autos':autos})

def direccion(request):
	return render(request, 'web/direccion.html')