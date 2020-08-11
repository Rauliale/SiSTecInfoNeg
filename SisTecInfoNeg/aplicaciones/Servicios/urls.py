from django.urls import path,re_path
from aplicaciones.Servicios.views import Home,crearServicio,editarServicio,crearTipoEquipo,editarTipoEquipo
#,crearMarca,listarMarcas,listarTipoEquipo
#listarServicio    incluir esto cuando descomente el path de listar servicio
urlpatterns = [ 
    path('crear_servicio/',crearServicio, name= 'crear_servicio'), #Crear servicio
    path('editar_servicio/<int:codServicio>',editarServicio, name= 'editar_servicio'),
    path('editar_Tipo_Equipo/<int:id>',editarTipoEquipo, name= 'editar_Tipo_Equipo'),
    #path('listar_servicio/',listarServicio, name= 'listar_servicio'),
    #path('crear_marca/',crearMarca, name= 'crear_marca'),
    #path('listar_marcas/',listarMarcas, name= 'listar_marcas'),
    path('crear_tipo_equipo/',crearTipoEquipo, name= 'crear_tipo_equipo'),
    #path('listar_tipo_equipo/',listarTipoEquipo, name= 'listar_tipo_equipo'),
    #path('',Home,name = 'index'),

]

