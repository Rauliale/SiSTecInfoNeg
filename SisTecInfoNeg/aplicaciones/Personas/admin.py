from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Domicilio)
admin.site.register(Tipo_Telefono)
admin.site.register(Telefono)
admin.site.register(Rol)
admin.site.register(Especialidad)


