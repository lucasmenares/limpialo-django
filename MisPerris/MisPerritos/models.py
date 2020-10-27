from django.db import models

# Create your models here.
class SliderPhoto(models.Model):
    nombre = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='car',null=False)

    def __str__(self):
        return self.nombre

class MisionVision(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()
    

    def __str__(self):
        return self.ident

class SliderGaleria(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='car',null=True)
    texto = models.CharField(max_length=65)

    def __str__(self):
        return self.ident

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