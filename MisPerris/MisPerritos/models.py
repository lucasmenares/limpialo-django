from django.db import models

# Create your models here.
class SliderPhoto(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='car',null=False)

    def __str__(self):
        return self.name

class Mision(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField(max_length=450)
    image = models.ImageField(upload_to='car',null=False)
    
    def __str__(self):
        return self.title

class Nosotros(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField(max_length=450)
    image = models.ImageField(upload_to='car',null=False)

    def __str__(self):
        return self.title

class GaleryPhoto(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='car',null=False)

    def __str__(self):
        return self.title

#Formulario
class Usuario(models.Model):
    nombre = models.TextField(max_length=80)
    apellido = models.TextField(max_length=80)
    email = models.CharField(max_length=80,primary_key=True)
    usuario = models.CharField(max_length=80)
    contrasena = models.CharField(max_length=80)
    confirmar = models.CharField(max_length=80)

    def __str__(self):
        return self.email

class Insumo(models.Model):
    nombre = models.TextField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre