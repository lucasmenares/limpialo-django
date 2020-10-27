from django.contrib import admin
from .models import SliderPhoto,Nosotros,Mision,SliderGaleria,Usuario,Insumo

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
admin.site.register(SliderPhoto)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Mision)
admin.site.register(SliderGaleria)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Insumo, InsumoAdmin)