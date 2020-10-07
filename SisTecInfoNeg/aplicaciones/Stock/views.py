from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

from django.contrib import messages


################################################################################################################
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from aplicaciones.Stock.forms import ArticuloForm
from aplicaciones.Stock.models import Articulo
#from apps.mixins import ValidatePermissionRequiredMixin

################################################################################################################

# Create your views here.

##################################################### Categoria ###########################################################
#Crear Categoria
def crearCategoria(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST) #recibe todos los datos del formulario
        if categoria_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            categoria_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/crear_categoria')    #redireccionar al index
    else:
        categoria_form = CategoriaForm()
    return render(request,'Stock/crear_categoria.html',{'categoria_form':categoria_form,'categorias':categorias})


#Editar Categoria
def editarCategoria(request,id):
    categorias = Categoria.objects.all()
    categoria_form = None 
    categoria = Categoria.objects.get(id = id) 
    if request.method == 'GET':
        categoria_form = CategoriaForm(instance = categoria)      
    else:
        categoria_form = CategoriaForm(request.POST, instance = categoria)
        if categoria_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            categoria_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/listar_categorias',{'categoria_form':categoria_form,'categorias':categorias,'categoria':categoria})    #redireccionar al index
    return render(request,'Stock/editar_categoria.html',{'categoria_form':categoria_form,'categorias':categorias,'categoria':categoria})


def eliminarCategoria (request,id):
    categorias = Categoria.objects.all()
    categoria_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        categoria = Categoria.objects.get(id = id) 
        categoria.delete()
        return redirect('/Stock/crear_categoria',{'categoria_form' : categoria_form, 'categorias':categorias})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Stock/listar_categorias.html',{'categoria_form' : categoria_form, 'categorias':categorias})


#listar Categoria
def listarCategorias(request):
    categorias = Categoria.objects.all()
    return render(request,'Stock/listar_categorias.html',{'categorias':categorias})
################################################################################################################

##################################################### Grupo ###########################################################
#Crear Grupo
def crearGrupo(request):
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        grupo_form = GrupoForm(request.POST) #recibe todos los datos del formulario
        if grupo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            grupo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/crear_grupo')    #redireccionar al index
    else:
        grupo_form = GrupoForm()
    return render(request,'Stock/crear_grupo.html',{'grupo_form':grupo_form,'grupos':grupos})


#Editar Grupo
def editarGrupo(request,id):
    grupos = Grupo.objects.all()
    grupo_form = None 
    grupo = Grupo.objects.get(id = id) 
    if request.method == 'GET':
        grupo_form = GrupoForm(instance = grupo)      
    else:
        grupo_form = GrupoForm(request.POST, instance = grupo)
        if grupo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            grupo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/listar_grupos',{'grupo_form':grupo_form,'grupos':grupos,'grupo':grupo})    #redireccionar al index
    return render(request,'Stock/editar_grupo.html',{'grupo_form':grupo_form,'grupos':grupos,'grupo':grupo})


def eliminarGrupo (request,id):
    grupos = Grupo.objects.all()
    grupo_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        grupo = Grupo.objects.get(id = id) 
        grupo.delete()
        return redirect('/Stock/crear_grupo',{'grupo_form' : grupo_form, 'grupos':grupos})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Stock/listar_grupos.html',{'grupo_form' : grupo_form, 'grupos':grupos})


#listar Grupos
def listarGrupos(request):
    grupos = Grupo.objects.all()
    return render(request,'Stock/listar_grupos.html',{'grupos':grupos})
################################################################################################################

############################################################## Movimientos ###################################################
#Registrar Ingreso
def regisrarIngreso(request):
    movimientos = Movimiento.objects.all()
    articulos = Articulo.objects.all() #aca ver deobtener equipos de una persona particular
    if request.method == 'POST':
        movimiento_form = MovimientoForm(request.POST) #recibe todos los datos del formulario
        articulo_form = ArticuloForm(request.POST) #recibe todos los datos del formulario
        print(movimiento_form.errors)
        if movimiento_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            movimiento_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/registrar_ingreso')    #redireccionar para volver a cargar otro servicio
    else:
        movimiento_form = MovimientoForm()
        articulo_form = ArticuloForm()
    return render(request,'Stock/registrar_ingreso.html',{'movimiento_form':movimiento_form,'articulo_form':articulo_form,'movimientos':movimientos,'articulos':articulos})

#Regisrar Salida
def regisrarSalida(request,id,baja):
    movimientos = Movimiento.objects.all()
    articulos = Articulo.objects.all()
    movimiento_form = None
    articulo_form = None
    movimiento = Movimiento.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    articulo = Articulo.objects.get(id = id)
    articulo.cantidad = articulo.cantidad - baja
    #articulo.precioDolar = 
    if request.method == 'GET':
        movimiento_form = MovimientoForm(instance = movimiento)       #ver de que es este instance = ??????????????????????????
        articulo_form = ArticuloForm(instance = articulo)
    else:
        movimiento_form = MovimientoForm(request.POST, instance = movimiento)
        articulo_form = ArticuloForm(request.POST, instance = articulo)
        if movimiento_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            movimiento_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            messages.success(request, 'Se editó correctamente')
            return redirect('/Stock/listar_movimientos',{'movimiento_form':movimiento_form,'articulo_form':articulo_form,'movimientos':movimientos,'articulo':articulo})    #redireccionar al index
        else:       
             messages.error(request, 'Ocurrió un error')    
    return render(request,'Stock/registrar_salida.html',{'movimiento_form':movimiento_form,'articulo_form':articulo_form,'movimientos':movimientos,'articulo':articulo})



#Eliminar un Movimiento
def eliminarMovimiento (request,id):
    movimientos = Movimiento.objects.all()
    movimiento_form=None
    try:
        equip = get_object_or_404(Movimiento,id=id)
        equip.delete()
        messages.warning(request, 'Se eliminó el Movimiento')
        return redirect('/Stock/crear_movimiento',{'movimiento_form' : movimiento_form, 'movimientos':movimientos})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el movimiento')
    return render(request, 'Stock/crear_movimiento.html',{'movimiento_form' : movimiento_form, 'movimientos':movimientos})

#listar Movimientos
def listarMovimientos(request):
    movimientos = Movimiento.objects.all()
    return render(request,'Stock/listar_movimientos.html',{'movimientos':movimientos})
#################################################################################################################


##################################################### Tipo de movimiento ###########################################################
#Crear Tipo de movimiento
def crearTipoMovimiento(request):
    tipo_movimientos = TipoMovimiento.objects.all()
    if request.method == 'POST':
        tipo_movimiento_form = TipoMovimientoForm(request.POST) #recibe todos los datos del formulario
        if tipo_movimiento_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipo_movimiento_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/crear_tipo_movimiento')    #redireccionar al index
    else:
        tipo_movimiento_form = TipoMovimientoForm()
    return render(request,'Stock/crear_tipo_movimiento.html',{'tipo_movimiento_form':tipo_movimiento_form,'tipo_movimientos':tipo_movimientos})


#Editar Tipo de movimiento
def editarTipoMovimiento(request,id):
    tipo_movimientos = TipoMovimiento.objects.all()
    tipo_movimiento_form = None 
    tipo_movimiento = TipoMovimiento.objects.get(id = id) 
    if request.method == 'GET':
        tipo_movimiento_form = TipoMovimientoForm(instance = tipo_movimiento)      
    else:
        tipo_movimiento_form = TipoMovimientoForm(request.POST, instance = tipo_movimiento)
        if tipo_movimiento_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipo_movimiento_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/listar_tipo_movimientos',{'tipo_movimiento_form':tipo_movimiento_form,'tipo_movimientos':tipo_movimientos,'tipo_movimiento':tipo_movimiento})    #redireccionar al index
    return render(request,'Stock/editar_tipo_movimiento.html',{'tipo_movimiento_form':tipo_movimiento_form,'tipo_movimientos':tipo_movimientos,'tipo_movimiento':tipo_movimiento})


def eliminarTipoMovimiento (request,id):
    tipo_movimientos = TipoMovimiento.objects.all()
    tipo_movimiento_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        tipo_movimiento = TipoMovimiento.objects.get(id = id) 
        tipo_movimiento.delete()
        return redirect('/Stock/crear_tipo_movimiento',{'tipo_movimiento_form' : tipo_movimiento_form, 'tipo_movimientos':tipo_movimientos})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Stock/listar_tipo_movimientos.html',{'tipo_movimiento_form' : tipo_movimiento_form, 'tipo_movimientos':tipo_movimientos})


#listar Tipos de Movimientos
def listarTipoMovimientos(request):
    tipo_movimientos = TipoMovimiento.objects.all()
    return render(request,'Stock/listar_tipo_movimientos.html',{'tipo_movimientos':tipo_movimientos})
################################################################################################################


##################################################### Unidad ###########################################################
#Crear Unidad
def crearUnidad(request):
    unidades = Unidad.objects.all()
    if request.method == 'POST':
        unidad_form = UnidadForm(request.POST) #recibe todos los datos del formulario
        if unidad_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            unidad_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/crear_unidad')    #redireccionar al index
    else:
        unidad_form = UnidadForm()
    return render(request,'Stock/crear_unidad.html',{'unidad_form':unidad_form,'unidades':unidades})


#Editar Unidad
def editarUnidad(request,id):
    unidades = Unidad.objects.all()
    unidad_form = None 
    unidad = Unidad.objects.get(id = id) 
    if request.method == 'GET':
        unidad_form = UnidadForm(instance = unidad)      
    else:
        unidad_form = UnidadForm(request.POST, instance = unidad)
        if unidad_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            unidad_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/listar_unidades',{'unidad_form':unidad_form,'unidades':unidades,'unidad':unidad})    #redireccionar al index
    return render(request,'Stock/editar_unidad.html',{'unidad_form':unidad_form,'unidades':unidades,'unidad':unidad})


def eliminarUnidad (request,id):
    unidades = Unidad.objects.all()
    unidad_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        unidad = Unidad.objects.get(id = id) 
        unidad.delete()
        return redirect('/Stock/crear_unidad',{'unidad_form' : unidad_form, 'unidades':unidades})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Stock/listar_unidades.html',{'unidad_form' : unidad_form, 'unidades':unidades})


#listar Unidades
def listarUnidades(request):
    unidades = Unidad.objects.all()
    return render(request,'Stock/listar_unidades.html',{'unidades':unidades})
################################################################################################################

##################################################### Articulo ###########################################################
#Crear Articulo
def crearArticulo(request):
    articulos = Articulo.objects.all()
    if request.method == 'POST':
        articulo_form = ArticuloForm(request.POST) #recibe todos los datos del formulario
        if articulo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            articulo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/crear_articulo')    #redireccionar al index
    else:
        articulo_form = ArticuloForm()
    return render(request,'Stock/crear_articulo.html',{'articulo_form':articulo_form,'articulos':articulos})


#Editar Articulo
def editarArticulo(request,id):
    articulos = Articulo.objects.all()
    articulo_form = None 
    articulo = Articulo.objects.get(id = id) 
    if request.method == 'GET':
        articulo_form = ArticuloForm(instance = articulo)      
    else:
        articulo_form = ArticuloForm(request.POST, instance = articulo)
        if articulo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            articulo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Stock/listar_articulos',{'articulo_form':articulo_form,'articulos':articulos,'articulo':articulo})    #redireccionar al index
    return render(request,'Stock/editar_articulo.html',{'articulo_form':articulo_form,'articulos':articulos,'articulo':articulo})


def eliminarArticulo (request,id):
    articulos = Articulo.objects.all()
    articulo_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        articulo = Articulo.objects.get(id = id) 
        articulo.delete()
        return redirect('/Stock/crear_articulo',{'articulo_form' : articulo_form, 'articulos':articulos})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Stock/listar_articulos.html',{'articulo_form' : articulo_form, 'articulos':articulos})


#listar Articulos
def listarArticulos(request):
    articulos = Articulo.objects.all()
    return render(request,'Stock/listar_articulos.html',{'articulos':articulos})
################################################################################################################


############################################### vistas basadas en clases ##############################

def articulos_list(request):
    data = {
        'title': 'Listado de Articulos',
        'articulos': Articulo.objects.all()
    }
    return render(request, 'Stock/list.html', data)


class ArticulosListView(ListView):
    model = Articulo
    template_name = 'Stock/list.html'
    permission_required = 'carreras.view_articulos'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Articulo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Articulo'
        context['create_url'] = reverse_lazy('Stock:articulo_create')
        context['list_url'] = reverse_lazy('Stock:articulo_list')
        context['entity'] = 'Articulo'
        return context


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'Stock/create_articulo.html'
    success_url = reverse_lazy('Stock:articulo_list')
    #permission_required = 'carreras.add_materias'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #MODO NORMAL
    #def post(self, request, *args, **kwargs):
    #    data = {}
    #    try:
    #        action = request.POST['action']
    #        if action == 'add':
    #            form = MateriasForm(request.POST)
    #            form = self.get_form()
    #            data = form.save()
    #        else:
    #            data['error'] = 'No ha ingresado ninguna opción'
    #    except Exception as e:
    #        data['error'] = str(e)
    #    return JsonResponse(data)

    #Modo con AJAX para controlar los años en el combobox
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_anios_id':
                carrera = Carreras.objects.get(pk=request.POST['id'])
                #print(carrera.duracion)
                anios = carrera.duracion
                print(anios)
                data = [{'id': '', 'text': '---------'}]
                #for i in AnioCursado.objects.filter(nombre=request.POST['id']):
                for i in AnioCursado.objects.filter(nombre__gte=1, nombre__lte=anios):
                    data.append({'id': i.id, 'text': i.nombre})
            elif action == 'add':
                form = ArticuloForm(request.POST)
                if form.is_valid():
                    form = self.get_form()
                    data = form.save()
                return redirect('Stock:articulo_list')
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Articulo'
        context['entity'] = 'Articulo'
        context['list_url'] = reverse_lazy('Stock:articulo_list')
        context['action'] = 'add'
        return context


class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'Stock/create_articulo.html'
    success_url = reverse_lazy('Stock:articulo_list')
    #permission_required = 'carreras.change_materias'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Materia'
        context['entity'] = 'Articulo'
        context['list_url'] = reverse_lazy('Stock:articulo_list')
        context['action'] = 'edit'
        return context

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'Stock/delete.html'
    success_url = reverse_lazy('Stock:articulo_list')
    #permission_required = 'carreras.delete_materias'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Materia'
        context['entity'] = 'Articulo'
        context['list_url'] = reverse_lazy('Stock:articulo_list')
        return context