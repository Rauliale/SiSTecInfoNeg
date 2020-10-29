from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo

class ArticuloAdmin(ImportExportModelAdmin,admin.ModelAdmin):     #sirve para el sitio de administracion de djngo editamos la vista del sitio de administracion
    search_fields = ['nombre']              #sirve para agregar una barra de busqueda y lo que esta dentro del [] es el atributo por el cual buscamos
    resources_class = ArticuloResource
    #list_display = ('nombre','estado')     #Sirve para decir que atributos van a ser mostrados en el sitio admin de djgo y van entre ()


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Grupo)
admin.site.register(Unidad)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(TipoMovimiento)
admin.site.register(TipoComprobante)
admin.site.register(LugarAlmacen)
admin.site.register(Movimiento)
admin.site.register(TipoImpuesto)
admin.site.register(Ganancias)


