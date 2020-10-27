from django.contrib import admin
from .models import SliderPhoto,Nosotros,Mision,GaleryPhoto,Usuario,Insumo

admin.site.site_header = 'Admin Limpialo'
admin.site.site_title = 'Bienvenido al panel de administracion de Limpialo'

class SliderPhotoAdmin(admin.ModelAdmin):
    list_display= ['title','image', 'created']
    search_fields= ['title','image', 'created']
    list_filter=['created']
    list_per_page=10

class MisionAdmin(admin.ModelAdmin):
    list_display= ['title','text','image']
    search_fields= ['title','text','image']
    #list_filter=[]
    list_per_page=10

class GaleryPhotoAdmin(admin.ModelAdmin):
    list_display= ['title','image']
    search_fields= ['title','image']
    #list_filter=[]
    list_per_page=10

class UsuarioAdmin(admin.ModelAdmin):
    list_display= ['nombre','apellido','email', 'usuario']
    search_fields= ['nombre','apellido','email','usuario']
    #list_filter=[]
    list_per_page=10

class InsumoAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','descripcion','stock']
    search_fields= ['nombre','precio','descripcion','stock']
    #list_filter=[]
    list_per_page=10

class NosotrosAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(SliderPhoto, SliderPhotoAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(GaleryPhoto, GaleryPhotoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Insumo, InsumoAdmin)