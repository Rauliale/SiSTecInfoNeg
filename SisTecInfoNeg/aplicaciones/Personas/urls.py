from django.urls import path
from aplicaciones.Personas.views import *

urlpatterns = [
    path('crear_provincia/',crearProvincia, name= 'crear_provincia'), #Crear Provincia
    path('listar_provincia/',listarProvincia, name= 'listar_provincia'), #listar Provincia
    path('editar_provincia/<int:id_provincia>',editarProvincia, name= 'editar_provincia'),
    path ('eliminar_provincia/<int:id_provincia>',eliminarProvincia,name='eliminar_provincia'),

    path('crear_localidad/',crearLocalidad, name= 'crear_localidad'), #Crear Localidad
    path('listar_localidad/',listarLocalidad, name= 'listar_localidad'), #listar Localidad 
    path('editar_localidad/<int:id_localidad>',editarLocalidad, name= 'editar_localidad'),
    path ('eliminar_localidad/<int:id_localidad>',eliminarLocalidad,name='eliminar_localidad'),

    path('crear_cliente/',crearCliente, name= 'crear_cliente'), #Crear Cliente
    path('listar_cliente/',listarCliente, name= 'listar_cliente'), #listar cliente

    path('crear_tecnico/',crearTecnico, name= 'crear_tecnico'), #Crear Tecnico
    path('listar_tecnico/',listarTecnico, name= 'listar_tecnico'), #listar cliente

    path('crear_empleado/',crearEmpleado, name= 'crear_empleado'), #Crear Empleado
    path('listar_empleado/',listarEmpleado, name= 'listar_empleado'), #listar Empleado
    #path('',Home,name = 'index')
]

