from django.shortcuts import render
from .models import SliderPhoto,Nosotros,Mision,GaleryPhoto,Insumo,TypeContact,Contact
# Import Modelo de tablas User
from django.contrib.auth.models import User
# Import Libreria de autentificacion
from django.contrib.auth import authenticate,logout,login as login_auth
#Import decorador para impedir ingreso de paginas sin estar registrado
from django.contrib.auth.decorators import login_required,permission_required

# Permite consumir servicios
import requests


#Import para acceso de token desde javascript, posterior almacenamiento
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from fcm_django.models import FCMDevice
# creación
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
	body = request.body.decode('utf-8')
	bodyDatos = json.loads(body)
	token = bodyDatos['token']
	# para evitar almaceanr 2 veces el mismo token
	existe = FCMDevice.objects.filter(registration_id=token,active=True)
	if len(existe)>0:
		return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe'}))
	dispo = FCMDevice()
	dispo.registration_id = token
	dispo.active = True
	# si el usuario está autentificado se puede almacenar
	if request.user.is_authenticated:
		dispo.user = request.user
	try:
		dispo.save()
		return HttpResponse(json.dumps({'mensaje':'Token almacenado'}))
	except:
		return HttpResponseBadRequest(json.dumps({'mensaje':'El token no se pudo almacenar'}))
		
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

@login_required(login_url='/login/')
@permission_required('MisPerris.add_insumo',login_url='/login/')
def admin_insumo(request):
	response = requests.get('http://127.0.0.1:8000/api/insumos/')
	insumos = response.json()
	if request.POST:
		action = request.POST.get("action")
		if action == "update":
			name = request.POST.get("name")
			price = request.POST.get("price")
			description = request.POST.get("description")
			stock = request.POST.get("stock")
			try:
				ins = Insumo.objects.get(name=name)
				ins.name=name
				ins.price=price
				ins.description=description
				ins.stock=stock
				ins.save()
				message = "Insumo modificado correctamente"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})
			except :
				message = "No se pudo modificar el insumo"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'error':message})
		if action == "delete":
			name = request.POST.get("name")
			try:
				i = Insumo.objects.get(name=name)
				i.delete()
				message="El insumo se elimino correctamente"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})
			except :
				message = "No se encontro el insumo que desea eliminar"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'error':message})
		if action == "register":
			name = request.POST.get("name")
			price = request.POST.get("price")
			description = request.POST.get("description")
			stock = request.POST.get("stock")
			try:
				i = Insumo.objects.get(name=name)
				message = "Insumo que desea agregar ya existe"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'error':message})
			except:
				'''ins = Insumo(
					name=name,
					price=price,
					description=description,
					stock=stock
				)
				ins.save()'''
				api_data = {
					'name':name,
					'price':price,
					'description':description,
					'stock':stock
				}
				response = requests.post('http://127.0.0.1:8000/api/insumos/',data=api_data)
				#enviar notificacion
				dispositivo = FCMDevice.objects.filter(active=True)
				dispositivo.send_message(
					title='Nuevo Insumo',
					body='Se ingresó el insumo: ' + name + ', con stock: ' + stock + ' y precio: ' + price, 
					icon='/static/images/favicon.png'
				)
				message = "Insumo se grabo correctamente"
				return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})
	return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos})

@login_required(login_url='/login/')
@permission_required('MisPerris.add_insumo',login_url='/login/')
def delete_insumo(request,id):
	try:
		ins = Insumo.objects.get(id=id)
		ins.delete()
		message = "Insumo eliminado correctamente"
		response = requests.get('http://127.0.0.1:8000/api/insumos/')
		insumos = response.json()
		return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})
	except:
		message = "No se pudo eliminar el insumo"
		response = requests.get('http://127.0.0.1:8000/api/insumos/')
		insumos = response.json()
		return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'error':message})
	response = requests.get('http://127.0.0.1:8000/api/insumos/')
	insumos = response.json()
	return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos})

@login_required(login_url='/login/')
@permission_required('MisPerris.add_insumo',login_url='/login/')
def modify_insumo(request,name):
		try:
			ins = Insumo.objects.get(name=name)
			return render(request,'web/admin/modify_insumos.html',{'item':ins})
		except:
			insumos = Insumo.objects.all()
			return render(request, 'web/admin/modify_insumos.html', {'lista_insumos':insumos})

@login_required(login_url='/login/')
@permission_required('MisPerris.add_insumo',login_url='/login/')
def update(request):
	if request.POST:
		name = request.POST.get("name")
		price = request.POST.get("price")
		description = request.POST.get("description")
		stock = request.POST.get("stock")
		try:
			ins = Insumo.objects.get(name=name)
			ins.name=name
			ins.price=price
			ins.description=description
			ins.stock=stock
			ins.save()
			insumos = Insumo.objects.all()
			message = "Insumo modificado correctamente"
			return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})
		except :
			insumos = Insumo.objects.all()
			message = "No se pudo modificar el insumo"
			return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'error':message})

def name_filter_api(request):
	name = request.POST.get("txtName")
	response = requests.get("http://127.0.0.1:8000/api/insumos/name/"+name+"/")
	insumos = response.json()
	message = "Filtrado"
	return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})

def price_filter_api(request):
	price = request.POST.get("txtPrice")
	response = requests.get("http://127.0.0.1:8000/api/insumos/price/"+price+"/")
	insumos = response.json()
	message = "Filtrado"
	return render(request, 'web/admin/admin_insumos.html', {'lista_insumos':insumos,'success':message})

def contacto(request):
	tipoContacto = TypeContact.objects.all()
	if request.POST:
		name = request.POST.get("name")
		lastname = request.POST.get("lastname")
		subject = request.POST.get("subject")
		ctype = request.POST.get("ctype")
		message = request.POST.get("message")
		obj_ctype = TypeContact.objects.get(name=ctype)
		cont = Contact(
			name=name,
			lastname=lastname,
			subject=subject,
			ctype= obj_ctype,
			message= message
		)
		cont.save()
		message = "Contacto se envió correctamente"
		dispositivo = FCMDevice.objects.filter(active=True)
		dispositivo.send_message(
			title='Nuevo Contacto',
			body='Se ingresó el contacto: ' + name + ', con Tipo: ' + ctype + ' y Asunto: ' + subject,
			icon='/static/images/favicon.png'
		)
		return render(request, 'web/index.html', {'tipo_contacto':tipoContacto,'success':message})
	return render(request, 'web/contacto.html',{'tipo_contacto':tipoContacto})