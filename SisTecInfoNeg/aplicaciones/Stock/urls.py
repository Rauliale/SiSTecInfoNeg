from django.urls import path,re_path
from aplicaciones.Stock.views import *
urlpatterns = [ 

############################# ABM Categorias #####################################
    path('crear_categoria/',crearCategoria, name= 'crear_categoria'),
    path('listar_categorias/',listarCategorias, name= 'listar_categorias'),
    path('editar_categoria/<int:id>',editarCategoria, name= 'editar_categoria'),
    path('eliminar_categoria/<int:id>',eliminarCategoria, name= 'eliminar_categoria'),

############################# ABM Grupos #####################################
    path('crear_grupo/',crearGrupo, name= 'crear_grupo'),
    path('listar_grupos/',listarGrupos, name= 'listar_grupos'),
    path('editar_grupo/<int:id>',editarGrupo, name= 'editar_grupo'),
    path('eliminar_grupo/<int:id>',eliminarGrupo, name= 'eliminar_grupo'),

############################# ABM Unidades #####################################
    path('crear_unidad/',crearUnidad, name= 'crear_unidad'),
    path('listar_unidades/',listarUnidades, name= 'listar_unidades'),
    path('editar_unidad/<int:id>',editarUnidad, name= 'editar_unidad'),
    path('eliminar_unidad/<int:id>',eliminarUnidad, name= 'eliminar_unidad'),

############################# ABM Articulos #####################################
    path('crear_articulo/',crearArticulo, name= 'crear_articulo'),
    path('listar_articulos/',listarArticulos, name= 'listar_articulos'),
    path('editar_articulo/<int:id>',Articulo, name= 'editar_articulo'),
    path('eliminar_articulo/<int:id>',eliminarArticulo, name= 'eliminar_articulo'),

############################# ABM Unidades #####################################
    path('crear_tipo_movimiento/',crearTipoMovimiento, name= 'crear_tipo_movimiento'),
    path('listar_tipo_movimientos/',listarTipoMovimientos, name= 'listar_tipo_movimientos'),
    path('editar_tipo_movimiento/<int:id>',editarTipoMovimiento, name= 'editar_tipo_movimiento'),
    path('eliminar_tipo_movimiento/<int:id>',eliminarTipoMovimiento, name= 'eliminar_tipo_movimiento'),

############################# ABM Movimientos #####################################
    path('listar_movimientos/',listarMovimientos, name= 'listar_movimientos'),
    path('registrar_ingreso/',regisrarIngreso, name= 'registrar_ingreso'),
    path('registrar_salida/<int:id>/<int:baja>',regisrarSalida, name= 'registrar_salida'),
    path('eliminar_movimiento/<int:id>',eliminarMovimiento, name= 'eliminar_movimiento'),


    
]