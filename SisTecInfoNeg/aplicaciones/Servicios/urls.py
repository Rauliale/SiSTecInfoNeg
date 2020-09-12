from django.urls import path,re_path
from aplicaciones.Servicios.views import *
#Home,crearServicio,editarServicio,crearTipoEquipo,editarTipoEquipo,eliminarTipoEquipo,listarTipoEquipo,crearEquipo,listarServicio,listarMarcas,crearMarca,crearEstadoEquipo,listarEstadoEquipo

urlpatterns = [ 
    ##################################### Wiki ############################################
    path('wiki/',Wiki, name = 'wiki'),
    path('crear_blog/',crearBlog, name = 'crear_blog'),
    path('leer_mas_blog/<int:id>',leerMasBlog, name= 'leer_mas_blog'),
    path('editar_blog/<int:id>',editarBlog, name= 'editar_blog'),
    path('listar_blog_categoria/<int:id>',listarBlogCategoria, name= 'listar_blog_categoria'),
    

    ############################ Pila de Servicios ###########################################
    path('listar_pila_servicio/',listarPilaServicio, name= 'listar_pila_servicio'),
    path('crear_pila_servicio/',crearPilaServicio, name= 'crear_pila_servicio'), #Crear servicio
    path('editar_pila_servicio/<int:codServicio>',editarPilaServicio, name= 'editar_pila_servicio'),
    path('eliminar_pila_servicio/<int:codServicio>',eliminarPilaServicio, name= 'eliminar_pila_servicio'),

    
    ############################ ABM Servicios ###########################################
    path('listar_servicio/',listarServicio, name= 'listar_servicio'),
    path('crear_servicio/',crearServicio, name= 'crear_servicio'), #Crear servicio
    path('editar_servicio/<int:codServicio>',editarServicio, name= 'editar_servicio'),
    path('eliminar_servicio/<int:codServicio>',eliminarServicio, name= 'eliminar_servicio'),
    
    ############################# ABM Tipo de Memoria #####################################
    path('crear_tipo_memoria/',crearTipoMemoria, name= 'crear_tipo_memoria'),
    path('listar_tipo_memoria/',listarTipoMemoria, name= 'listar_tipo_memoria'),
    path('editar_tipo_memoria/<int:id>',editarTipoMemoria, name= 'editar_tipo_memoria'),
    path('eliminar_tipo_memoria/<int:id>',eliminarTipoMemoria, name= 'eliminar_tipo_memoria'),

    ############################# ABM Tipo de Disco #####################################
    path('crear_tipo_disco/',crearTipoDisco, name= 'crear_tipo_disco'),
    path('listar_tipo_disco/',listarTipoDisco, name= 'listar_tipo_disco'),
    path('editar_tipo_disco/<int:id>',editarTipoDisco, name= 'editar_tipo_disco'),
    path('eliminar_tipo_disco/<int:id>',eliminarTipoDisco, name= 'eliminar_tipo_disco'),

    ############################# ABM Tipo de Equipo #####################################
    path('crear_tipo_equipo/',crearTipoEquipo, name= 'crear_tipo_equipo'),
    path('listar_tipo_equipo/',listarTipoEquipo, name= 'listar_tipo_equipo'),
    path('editar_tipo_equipo/<int:id>',editarTipoEquipo, name= 'editar_tipo_equipo'),
    path('eliminar_tipo_equipo/<int:id>',eliminarTipoEquipo, name= 'eliminar_tipo_equipo'),
    

    ############################ ABM Equipo #############################################
    path('crear_equipo/',crearEquipo, name= 'crear_equipo'),
    path('listar_equipo/',listarEquipo, name= 'listar_equipo'),
    path('editar_equipo/<int:id>',editarEquipo, name= 'editar_equipo'),
    path ('eliminar_equipo/<int:id>',eliminarEquipo,name='eliminar_equipo'),


    ############################ ABM MARCA #############################################
    path('listar_marcas/',listarMarcas, name= 'listar_marcas'),
    path('crear_marca/',crearMarca, name= 'crear_marca'),
    path('editar_marca/<int:id>',editarMarca, name= 'editar_marca'),
    path ('eliminar_marca/<int:id>',eliminarMarca,name='eliminar_marca'),

    ############################ ABM MARCA #############################################
    path('listar_accesorios/',listarAccesorio, name= 'listar_accesorios'),
    path('crear_accesorio/',crearAccesorio, name= 'crear_accesorio'),
    path('editar_accesorio/<int:id>',editarAccesorio, name= 'editar_accesorio'),
    path ('eliminar_accesorio/<int:id>',eliminarAccesorio,name='eliminar_accesorio'),

    ############################ ABM Estado de Equipo ##################################
    path('crear_estado_equipo/',crearEstadoEquipo, name= 'crear_estado_equipo'),
    path('listar_estado_equipo/',listarEstadoEquipo, name= 'listar_estado_equipo'),
    path('editar_estado_equipo/<int:id>',editarEstadoEquipo, name= 'editar_estado_equipo'),
    path ('eliminar_estado_equipo/<int:id>',eliminarEstadoEquipo,name='eliminar_estado_equipo'),

    ############################ ABM Estado de Repuesto ##################################
    path('crear_estado_repuesto/',crearEstadoRepuesto, name= 'crear_estado_repuesto'),
    path('listar_estado_repuesto/',listarEstadoRepuesto, name= 'listar_estado_repuesto'),
    path('editar_estado_repuesto/<int:id>',editarEstadoRepuesto, name= 'editar_estado_repuesto'),
    path ('eliminar_estado_repuesto/<int:id>',eliminarEstadoRepuesto,name='eliminar_estado_repuesto'),
    
    
   
     
    #path('',Home,name = 'index'),

]

