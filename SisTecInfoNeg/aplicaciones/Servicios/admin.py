from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class Servicio_TecnicoResource(resources.ModelResource):
    class Meta:
        model = Servicio_Tecnico

class Servicio_TecnicoAdmin(ImportExportModelAdmin,admin.ModelAdmin):     #sirve para el sitio de administracion de djngo editamos la vista del sitio de administracion
    search_fields = ['nombre']              #sirve para agregar una barra de busqueda y lo que esta dentro del [] es el atributo por el cual buscamos
    resources_class = Servicio_TecnicoResource
    #list_display = ('nombre','estado')     #Sirve para decir que atributos van a ser mostrados en el sitio admin de djgo y van entre ()

admin.site.register(Repuesto)
admin.site.register(Estado)
admin.site.register(TipoEquipo)
admin.site.register(Servicio_Tecnico,Servicio_TecnicoAdmin)
admin.site.register(Marca)
admin.site.register(Estado_Repuesto)
admin.site.register(Equipo)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Blog)