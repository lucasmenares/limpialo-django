from django.db import models

# Create your models here.
class SliderPhoto(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='car',null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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

class Insumo(models.Model):
    name = models.TextField(max_length=120)
    price = models.IntegerField()
    description = models.CharField(max_length=200,blank=True,null=True)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TypeContact(models.Model):
    name = models.CharField(max_length=60,primary_key=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    lastname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    ctype = models.ForeignKey(TypeContact,on_delete=models.DO_NOTHING)
    message = models.TextField(max_length=200)
    
    def __str__(self):
        return self.name