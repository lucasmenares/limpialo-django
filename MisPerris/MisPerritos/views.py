from django.shortcuts import render
from .models import SliderPhoto,Nosotros,Mision,GaleryPhoto,Usuario,Insumo
# Import Modelo de tablas User
from django.contrib.auth.models import User
# Import Libreria de autentificacion
from django.contrib.auth import authenticate,logout,login as login_auth
#Import decorador para impedir ingreso de paginas sin estar registrado
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	autos = SliderPhoto.objects.all()
	return render(request,'web/index.html',{'autos':autos})

def vision(request):
	nosotros = Nosotros.objects.first()
	mision = Mision.objects.all()
	return render(request,'web/vision.html',{'nosotros':nosotros,'mision':mision})

def registro(request):
	return render(request, 'web/registro/registro.html')

def usuario(request):
	if request.POST:
		name = request.POST.get("name")
		lastName = request.POST.get("lastname")
		email = request.POST.get("email")
		username = request.POST.get("username")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")

		user = User()
		user.first_name = name
		user.last_name = lastName
		user.email = email
		user.username = username
		user.set_password(password)
		user.save()
		mensaje = 'Grabado correctamente'
		return render(request,'web/registro/usuario.html',{'msg':mensaje})
	return render(request, 'web/registro/usuario.html')

@login_required(login_url='/login/')
def insumos(request):
	return render(request, 'web/registro/insumos.html')

def galeria(request):
	photos = GaleryPhoto.objects.all()
	return render(request,'web/galeria.html',{'photos':photos})

def direccion(request):
	return render(request, 'web/direccion.html')

def login(request):
	autos = SliderPhoto.objects.all()
	if request.POST:
		user = request.POST.get("name")
		password = request.POST.get("password")
		us = authenticate(request,username=user,password=password)
		if us is not None and us.is_active:
			login_auth(request,us)
			return render(request,'web/index.html',{'user':us,'autos':autos})
		else:
			return render(request,'web/usuario/login.html',{'msg':'usuario / contrasena incorrecta'})
	return render(request, 'web/usuario/login.html')

def logout_view(request):
	logout(request)
	return render(request,'web/usuario/login.html')