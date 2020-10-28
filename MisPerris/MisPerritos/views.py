from django.shortcuts import render
from .models import SliderPhoto,Nosotros,Mision,GaleryPhoto,Insumo
# Import Modelo de tablas User
from django.contrib.auth.models import User
# Import Libreria de autentificacion
from django.contrib.auth import authenticate,logout,login as login_auth
#Import decorador para impedir ingreso de paginas sin estar registrado
from django.contrib.auth.decorators import login_required,permission_required


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
	autos = SliderPhoto.objects.all()
	if request.POST:
		name = request.POST.get("name")
		lastName = request.POST.get("lastname")
		email = request.POST.get("email")
		username = request.POST.get("username")
		password = request.POST.get("password")
		password2 = request.POST.get("password2")
		try:
			user = User.objects.get(username=username)
			message = 'El nombre de usuario ya esta en uso'
			return render(request,'web/registro/usuario.html',{'error':message})
		except:
			try:
				user = User.objects.get(email=email)
				message = 'El correo ya esta en uso'
				return render(request,'web/registro/usuario.html',{'error':message})
			except:
				if password != password2:
					message = "Las contrasenas no coinciden"
					return render(request,'web/registro/usuario.html',{'error':message})
				user = User()
				user.first_name = name
				user.last_name = lastName
				user.email = email
				user.username = username
				user.set_password(password)
				user.save()
				message = 'Gracias por registrate ' + user.first_name + ' ' + user.last_name + ', Bienvenido a Limpialo'
				us = authenticate(request,username=user,password=password)
				login_auth(request,us)
				return render(request,'web/index.html',{'user':us,'autos':autos,'success':message})
	return render(request, 'web/registro/usuario.html')

@login_required(login_url='/login/')
@permission_required('MisPerris.add_insumo',login_url='/login/')
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
			message = "Ingresaste correctamente. Bienvenido a Limpialo " + us.first_name
			return render(request,'web/index.html',{'user':us,'autos':autos,'success':message})
		else:
			message = "Usuario o contrasena incorrectos"
			return render(request,'web/usuario/login.html',{'error':message})
	return render(request, 'web/usuario/login.html')

def logout_view(request):
	logout(request)
	message = "Cerraste sesion correctamente"
	return render(request,'web/usuario/login.html',{'success':message})