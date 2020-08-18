from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Empleado)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Domicilio)
admin.site.register(Tipo_Telefono)
admin.site.register(Telefono)
#admin.site.register(Usuario)
admin.site.register(Especialidad)


