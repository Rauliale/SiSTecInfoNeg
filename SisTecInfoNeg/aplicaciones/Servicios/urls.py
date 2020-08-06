from django.urls import path,re_path
from .views import home,crearServicio,listarServicio,editarServicio,crearMarca,listarMarcas,crearTipoEquipo,listarTipoEquipo

urlpatterns = [ 
    path('crear_servicio/',crearServicio, name= 'crear_servicio'),
    path('listar_servicio/',listarServicio, name= 'listar_servicio'),
    path('crear_marca/',crearMarca, name= 'crear_marca'),
    path('listar_marcas/',listarMarcas, name= 'listar_marcas'),
    path('crear_tipo_equipo/',crearTipoEquipo, name= 'crear_tipo_equipo'),
    path('listar_tipo_equipo/',listarTipoEquipo, name= 'listar_tipo_equipo'),
    path('editar_servicio/<int:codServicio>',editarServicio, name= 'editar_servicio'),
    path('',home,name = 'index'),

]

