from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from aplicaciones.configuracion.models import Configuracion
from aplicaciones.Personas.models import Cliente
from aplicaciones.Personas.forms import ClienteForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#Home
def Home(request):

    return render(request, 'index.html')

def Wiki(request):
    blogs = Blog.objects.filter(estado = True)
    categorias = Categoria.objects.all()
    return render(request,'wiki.html',{'blogs':blogs,'categorias':categorias})




############################################################## Blog ###################################################
def crearBlog(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST) #recibe todos los datos del formulario
        print(blog_form.errors)
        if blog_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            blog_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_blog')    #redireccionar para volver a cargar otro servicio
    else:
        blog_form = BlogForm()
    return render(request,'Wikis/crear_blog.html',{'blog_form':blog_form,'blogs':blogs})

def leerMasBlog(request,id):
    blogs = Blog.objects.all()
    blog_form = None 
    blog = Blog.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        blog_form = BlogForm(instance = blog)       #ver de que es este instance = ??????????????????????????
    else:
        blog_form = BlogForm(request.POST, instance = blog)
        if blog_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            blog_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/wiki',{'blog_form':blog_form,'blogs':blogs,'blog':blog})    #redireccionar al index
    return render(request,'Wikis/leer_mas_blog.html',{'blog_form':blog_form,'blogs':blogs,'blog':blog})

def editarBlog(request,id):
    blogs = Blog.objects.all()
    blog_form = None 
    blog = Blog.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        blog_form = BlogForm(instance = blog)       #ver de que es este instance = ??????????????????????????
    else:
        blog_form = BlogForm(request.POST, instance = blog)
        if blog_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            blog_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/wiki',{'blog_form':blog_form,'blogs':blogs,'blog':blog})    #redireccionar al index
    return render(request,'Wikis/editar_blog.html',{'blog_form':blog_form,'blogs':blogs,'blog':blog})

def listarBlogCategoria(request,id):
    blogcategoria = Blog.objects.all().filter(categoria=id)
    print(blogcategoria)
    return render(request,'Wikis/listar_blog_categoria.html',{'blogcategoria':blogcategoria})




############################################################## Servicio Tecnico ###################################################
#Crear Servicio Tecnico
def crearServicio(request):
    
    servicios = Servicio_Tecnico.objects.all()
    clientes = Cliente.objects.all()
    equipos = Equipo.objects.all() #aca ver deobtener equipos de una persona particular
    if request.method == 'POST':
        #if 'crear_equipo_modal' in request.POST:
        #        equipo_form = EquipoForm(request.POST) #recibe todos los datos del formulario
        #        if equipo_form.is_valid():
        #            equipo = equipo_form.save(commit = False)
        servicio_form = Servicio_TecnicoForm(request.POST) #recibe todos los datos del formulario
        #cliente_forms = ClienteForm(request.POST)
        
        print(servicio_form.errors)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            #cliente_forms.save()
            print("me redireccione")
            return redirect('/Servicios/crear_servicio')    #redireccionar para volver a cargar otro servicio
    else:
        servicio_form = Servicio_TecnicoForm()
        cliente_forms = ClienteForm()
        equipo_form = EquipoForm()
        print("por el modal?")
    reporte = Configuracion.objects.all().last()
    print(reporte)
    context = {'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipos':equipos,'reporte':reporte,'clientes':clientes,'cliente_forms':cliente_forms}
    return render(request,'Servicios/crear_servicio.html',context)


#Editar un Servicio
def editarServicio(request,codServicio):
    servicios = Servicio_Tecnico.objects.all()
    equipo = Equipo.objects.all()
    servicio_form = None
    equipo_form = None
    servicio = Servicio_Tecnico.objects.get(codServicio = codServicio) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    equi = servicio.equipo
    if request.method == 'GET':
        servicio_form = Servicio_TecnicoForm(instance = servicio)       #ver de que es este instance = ??????????????????????????
        equipo_form = EquipoForm(instance = equi)
    else:
        servicio_form = Servicio_TecnicoForm(request.POST, instance = servicio)
        equipo_form = EquipoForm(request.POST, instance = equi)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio = servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            equipo = equipo_form
            #messages.success(request, 'Se editó correctamente')
            #return redirect('/Servicios/listar_servicio',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo})    #redireccionar al index
            
            actualizar = 1
            clie = equipo.cliente.dni
            varid = equipo.id
            print(varid)
            return render(request,'Servicios/crear_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'equipo':equipo,'servicios':servicios,'marcas':marcas,'actualizar':actualizar,'varid':varid,'clie':clie})
        else:       
             messages.error(request, 'Ocurrió un error')    
    return render(request,'Servicios/editar_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo})

#Eliminar un Servicio
def eliminarServicio (request,id):
    servicios = Servicio_Tecnico.objects.all()
    servicio_form=None
    try:
        equip = get_object_or_404(Servicio_Tecnico,id=id)
        equip.delete()
        messages.warning(request, 'Se eliminó el Servicio Tecnico')
        return redirect('/Servicios/crear_equipo',{'servicio_form' : servicio_form, 'servicios':servicios})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el servicio tecnico')
    return render(request, 'Servicios/crear_servicio.html',{'servicio_form' : servicio_form, 'servicios':servicios})

#listar Servicio
def listarServicio(request):
    servicios = Servicio_Tecnico.objects.all()
    return render(request,'Servicios/listar_servicio.html',{'servicios':servicios})


@csrf_exempt
#Mostrar equipos de Clientes
def mostrarEquipos(request):
    id = request.GET.get('cliente',None)
    cliente = Cliente.objects.get(dni = id)
    result = dict()   
    equipos = cliente.equipo_set.all()  #aca obtengo una consulta de manera inversa re chevere
    serializer = EquipoSerializer(equipos, many=True)
    result = serializer.data
    return JsonResponse(result,safe=False)

@csrf_exempt
#devuelve los datos del equipo (marca,tipo equipo,modelo) a la pagina crear servicios
def mostrarMarca(request):
    id = request.GET.get('equipo',None)
    equipo = Equipo.objects.get(id = id)
    result = dict() 
    result = {
        'id':equipo.id,
        'modelo':equipo.modelo,
        'marca':equipo.marca.nombre,
        'tipoEquipo':equipo.tipoEquipo.nombre,
    }
    return JsonResponse(result,safe=False)

@csrf_exempt
#devuelve los datos del equipo (marca,tipoEquipo,modelo,cliente,equipo,fechaIngreso,) a la pagina editar servicios
def mostrarServicio(request):
    id = request.GET.get('equipo',None)
    equipo = Equipo.objects.get(id = id)
    result = dict() 
    result = {
        'id':equipo.id,
        'modelo':equipo.modelo,
        'marca':equipo.marca.nombre,
        'tipoEquipo':equipo.tipoEquipo.nombre,
    }
    return JsonResponse(result,safe=False)

@csrf_exempt
#Mostrar equipos de Clientes
def mostrarModelo(request):
    id = request.GET.get('equipo',None)
    equipo = Equipo.objects.get(id = id)
    print("mierda")
    print(equipo)
    result = dict()   
    modelo = equipo.modelo  #aca obtengo una consulta de manera inversa re chevere
    print("bandera")
    print(modelo)
    serializer = ModeloSerializer(modelo)
    print("Serialicer tiene ->")
    print(serializer)
    result = serializer.data
    print("Result tiene ->")
    print(result)
    return JsonResponse(result,safe=False)

#################################################################################################################

############################################################## Pila de Servicio Tecnico ###################################################
#Crear Servicio Tecnico
def crearPilaServicio(request):
    servicios = Servicio_Tecnico.objects.all()
    equipo = Equipo.objects.all()
    if request.method == 'POST':
        servicio_form = Servicio_TecnicoForm(request.POST) #recibe todos los datos del formulario
        equipo_form = EquipoForm(request.POST) #recibe todos los datos del formulario
        print(servicio_form.errors)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_pila_servicio')    #redireccionar para volver a cargar otro servicio
    else:
        servicio_form = Servicio_TecnicoForm()
        equipo_form = EquipoForm()
    return render(request,'Servicios/crear_pila_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo})

#Editar pila Servicio
def editarPilaServicio(request,codServicio):
    servicios = Servicio_Tecnico.objects.all()
    equipo = Equipo.objects.all()
    servicio_form = None
    equipo_form = None
    servicio = Servicio_Tecnico.objects.get(codServicio = codServicio) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    equi = servicio.equipo
    if request.method == 'GET':
        servicio_form = Servicio_TecnicoForm(instance = servicio)       #ver de que es este instance = ??????????????????????????
        equipo_form = EquipoForm(instance = equi)
    else:
        servicio_form = Servicio_TecnicoForm(request.POST, instance = servicio)
        equipo_form = EquipoForm(request.POST, instance = equi)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            messages.success(request, 'Se editó correctamente')
            return redirect('/Servicios/listar_pila_servicio',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo,'equi':equi,'servicio':servicio})    #redireccionar al index
        else:
            print(servicio_form)
            print("aca entro")       
            messages.error(request, 'Ocurrió un errorcito')    
    return render(request,'Servicios/editar_pila_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo,'equi':equi,'servicio':servicio})

#Editar pila Servicio modificado
def editarPilaServicio2(request,codServicio,id):
    servicio_form = None
    equipo_form = None
    servicio = Servicio_Tecnico.objects.get(codServicio = codServicio) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    equipo = Equipo.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    equi = servicio.equipo
    if request.method == 'GET':
        servicio_form = Servicio_TecnicoForm(instance = servicio)       #ver de que es este instance = ??????????????????????????
        equipo_form = EquipoForm(instance = equi)
    else:
        servicio_form = Servicio_TecnicoForm(request.POST, instance = servicio)
        equipo_form = EquipoForm(request.POST, instance = equi)
        if servicio_form.is_valid() and equipo_form.is_valid() :    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            equipo_form.save()
            messages.success(request, 'Se editó correctamente')
            return redirect('/Servicios/listar_pila_servicio',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo,'equi':equi,'servicio':servicio})    #redireccionar al index
        else:
            print("aca entro")       
            messages.error(request, 'Ocurrió un errorcito')    
    return render(request,'Servicios/editar_pila_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'equipo':equipo,'equi':equi,'servicio':servicio})


#Eliminar un Servicio
def eliminarPilaServicio (request,id):
    servicios = Servicio_Tecnico.objects.all()
    servicio_form=None
    try:
        equip = get_object_or_404(Servicio_Tecnico,id=id)
        equip.delete()
        messages.warning(request, 'Se eliminó el Servicio Tecnico')
        return redirect('/Servicios/crear_pila_equipo',{'servicio_form' : servicio_form, 'servicios':servicios})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el servicio tecnico')
    return render(request, 'Servicios/crear_pila_servicio.html',{'servicio_form' : servicio_form, 'servicios':servicios})

#listar Servicio
def listarPilaServicio(request):
    servicios = Servicio_Tecnico.objects.filter(estado=1)   #estado es 1 xq Recibido siempre va a ser mi primer estado
    print(servicios)
    return render(request,'Servicios/listar_pila_servicio.html',{'servicios':servicios})
#################################################################################################################



##################################################### Tipo Equipo ###########################################################
#Crear Tipo Equipo
def crearTipoEquipo(request):
    tipo_Equipo = TipoEquipo.objects.all()
    if request.method == 'POST':
        tipoEquipo_form = TipoEquipoForm(request.POST) #recibe todos los datos del formulario
        if tipoEquipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoEquipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_tipo_equipo')    #redireccionar al index
    else:
        tipoEquipo_form = TipoEquipoForm()
    return render(request,'Servicios/crear_tipo_equipo.html',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo})


#Editar Tipo Equipo
def editarTipoEquipo(request,id):
    tipo_Equipo = TipoEquipo.objects.all()
    tipoEquipo_form = None 
    tipo = TipoEquipo.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        tipoEquipo_form = TipoEquipoForm(instance = tipo)       #ver de que es este instance = ??????????????????????????
    else:
        tipoEquipo_form = TipoEquipoForm(request.POST, instance = tipo)
        if tipoEquipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoEquipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_tipo_equipo',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo,'tipo':tipo})    #redireccionar al index
    return render(request,'Servicios/editar_tipo_equipo.html',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo,'tipo':tipo})


def eliminarTipoEquipo (request,id):
    tipoEquipo = TipoEquipo.objects.all()
    tipoEquipo_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        tipoE = TipoEquipo.objects.get(id = id) 
        tipoE.delete()
        return redirect('/Servicios/crear_tipo_equipo',{'tipoEquipo_form' : tipoEquipo_form, 'tipoEquipo':tipoEquipo})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Servicios/listar_tipo_equipo.html',{'tipoEquipo_form' : tipoEquipo_form, 'tipoEquipo':tipoEquipo})


#listar Tipo Equipo
def listarTipoEquipo(request):
    tipo_Equipo = TipoEquipo.objects.all()
    return render(request,'Servicios/listar_tipo_equipo.html',{'tipo_Equipo':tipo_Equipo})
################################################################################################################


######################################################## Equipo ########################################################
#Crear Equipo
def crearEquipo(request):
    equipo = Equipo.objects.all()
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST) #recibe todos los datos del formulario
        print(equipo_form.errors)
        if equipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            equipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear el equipo')
            return redirect('crear_equipo')    #redireccionar al index
    
    else:
        equipo_form = EquipoForm()
    return render(request,'Servicios/crear_equipo.html',{'equipo_form':equipo_form,'equipo':equipo})    


#Crear Equipo Modal
def crearEquipoModal(request):
    equipo = Equipo.objects.all()
    servicios = Servicio_Tecnico.objects.all()
    marcas = Marca.objects.all()
    servicio_form = Servicio_TecnicoForm()
    if request.method == 'POST':
        equipo_form = EquipoForm(request.POST) #recibe todos los datos del formulario
        print(equipo_form.errors)
        if equipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            print("entro")
            equipo = equipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            
            actualizar = 1
            
            clie = equipo.cliente.dni

            varid = equipo.id
            print(varid)

            return render(request,'Servicios/crear_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'equipo':equipo,'servicios':servicios,'marcas':marcas,'actualizar':actualizar,'varid':varid,'clie':clie})
        else:
            print('Ocurrió un error al tratar de crear el equipo')
            print(servicios)
            return redirect('crear_servicio',{'servicios':servicios})    #redireccionar al index
    
    else:
        print('entro por aca')
        equipo_form = EquipoForm()
        servicio_form = Servicio_TecnicoForm()
        return render(request,'Servicios/crear_equipo_modal.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'equipo':equipo,'servicios':servicios,'marcas':marcas})    

#Editar equipo
def editarEquipo(request,id):
    equipo = Equipo.objects.all()
    equipo_form = None 
    equip = Equipo.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        equipo_form = EquipoForm(instance = equip)       #ver de que es este instance = ??????????????????????????
    else:
        equipo_form = EquipoForm(request.POST, instance = equip)
        if equipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            equipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_equipo',{'equipo_form':equipo_form,'equipo':equipo,'equip':equip})    #redireccionar al index
        else:      
             messages.error(request, 'Ocurrió un error')    
    return render(request,'Servicios/editar_equipo.html',{'equipo_form':equipo_form,'equipo':equipo,'equip':equip})

#Eliminar un Equipo
def eliminarEquipo (request,id):
    equipo = Equipo.objects.all()
    equipo_form=None
    try:
        equip = Equipo.objects.get(id = id)
        equip.delete()
        messages.warning(request, 'Se eliminó el Equipo')
        return redirect('/Servicios/crear_equipo',{'equipo_form' : equipo_form, 'equipo':equipo})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el país')
    return render(request, 'Servicios/listar_equipo.html',{'equipo_form' : equipo_form, 'equipo':equipo})


def listarEquipo(request):
    equipo = Equipo.objects.all()
    return render(request,'Servicios/listar_equipo.html',{'equipo':equipo})
################################################################################################################


######################################################## Crear Marca ########################################################
def crearMarca(request):
    marcas = Marca.objects.all()
    if request.method == 'POST':
        marca_form = MarcaForm(request.POST) #recibe todos los datos del formulario
        if marca_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            marca_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            print('Ocurrió un error al tratar de crear el equipo')
            return redirect('/Servicios/crear_marca')    #redireccionar al index
    else:
        marca_form = MarcaForm()
    return render(request,'Servicios/crear_marca.html',{'marca_form':marca_form,'marcas':marcas})

def crearMarcaModal(request):
    marcas = Marca.objects.all()
    equipo = Equipo.objects.all()
    servicios = Servicio_Tecnico.objects.all()
    if request.method == 'POST':
        marca_form = MarcaForm(request.POST) #recibe todos los datos del formulario
        if marca_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            marca_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            print('Ocurrió un error al tratar de crear el equipo')
            return redirect('/Servicios/crear_servicio')    #redireccionar al index
    else:
        marca_form = MarcaForm()
    marcas = Marca.objects.all()
    return render(request,'Servicios/crear_marca_modal.html',{'marca_form':marca_form,'marcas':marcas,'equipo':equipo,'servicios':servicios})


#Editar Marca
def editarMarca(request,id):
    marcas = Marca.objects.all()
    marca_form = None 
    marca = Marca.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        marca_form = MarcaForm(instance = marca)       #ver de que es este instance = ??????????????????????????
    else:
        marca_form = MarcaForm(request.POST, instance = marca)
        if marca_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            marca_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_marcas',{'marca_form':marca_form,'marcas':marcas,'marca':marca})    #redireccionar al index 
    print('lo que hay en marca es:')
    print(marca)
    return render(request,'Servicios/editar_marca.html',{'marca_form':marca_form,'marcas':marcas,'marca':marca})

#Eliminar una Marca
def eliminarMarca (request,id):
    marcas = Marca.objects.all()
    print(id)
    marca_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        marca = Marca.objects.get(id = id) 
        marca.delete()
        print('entro acá')
        messages.warning(request, 'Se eliminó la marca')
        return redirect('/Servicios/crear_marca',{'marca_form' : marca_form, 'marcas':marcas})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la marca ya que tiene equipos asociados')
        print('entro acá 2')#no está mandando el error al front end
    return render(request, 'Servicios/listar_marcas.html',{'marca_form' : marca_form, 'marcas':marcas})

def listarMarcas(request):
    marcas = Marca.objects.all()
    return render(request,'Servicios/listar_marcas.html',{'marcas':marcas})
################################################################################################################

######################################################## Accesorios ########################################################
#Crear Accesorio
def crearAccesorio(request):
    accesorios = Accesorio.objects.all()
    if request.method == 'POST':
        accesorio_form = AccesorioForm(request.POST) #recibe todos los datos del formulario
        if accesorio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            accesorio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            print('Ocurrió un error al tratar de crear accesorio')
            return redirect('/Servicios/crear_accesorio')    #redireccionar al index
    else:
        accesorio_form = AccesorioForm()
    return render(request,'Servicios/crear_accesorio.html',{'accesorio_form':accesorio_form,'accesorios':accesorios})
    
#Editar Accesorio
def editarAccesorio(request,id):
    accesorios = Accesorio.objects.all()
    accesorio_form = None 
    accesorio = Accesorio.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        accesorio_form = AccesorioForm(instance = accesorio)       #ver de que es este instance = ??????????????????????????
    else:
        accesorio_form = AccesorioForm(request.POST, instance = accesorio)
        if accesorio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            accesorio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_accesorios',{'accesorio_form':accesorio_form,'accesorios':accesorios,'accesorio':accesorio})    #redireccionar al index 

    return render(request,'Servicios/editar_accesorios.html',{'accesorio_form':accesorio_form,'accesorios':accesorios,'accesorio':accesorio})

#Eliminar una Accesorio
def eliminarAccesorio (request,id):
    accesorios = Accesorio.objects.all()
    print(id)
    accesorio_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        accesorio = Accesorio.objects.get(id = id) 
        accesorio.delete()
        print('entro acá')
        messages.warning(request, 'Se eliminó la accesorio')
        return redirect('/Servicios/crear_accesorio',{'accesorio_form' : accesorio_form, 'accesorio':accesorio})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la marca ya que tiene equipos asociados')
        print('entro acá 2')#no está mandando el error al front end
    return render(request, 'Servicios/listar_accesorios.html',{'accesorio_form' : accesorio_form, 'acesorios':acesorios})

def listarAccesorio(request):
    accesorios = Accesorio.objects.all()
    return render(request,'Servicios/listar_accesorios.html',{'accesorios':accesorios})
################################################################################################################





############################################### Estado Equipo ###################################################
#crear Estado Equipo
def crearEstadoEquipo(request):
    estadoEquipo = Estado.objects.all()
    if request.method == 'POST':
        estado_equipo_form = EstadoForm(request.POST) #recibe todos los datos del formulario
        if estado_equipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            estado_equipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            print('Ocurrió un error al tratar de crear el equipo')
            return redirect('/Servicios/crear_estado_equipo')    #redireccionar al index
    else:
        estado_equipo_form = EstadoForm()
    return render(request,'Servicios/crear_estado_equipo.html',{'estado_equipo_form':estado_equipo_form,'estadoEquipo':estadoEquipo})

#Editar un Estado de Equipo
def editarEstadoEquipo(request,id):
    estadoEquipo = Estado.objects.all()
    estado_equipo_form = None 
    estado = Estado.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        estado_equipo_form = EstadoForm(instance = estado)       #ver de que es este instance = ??????????????????????????
    else:
        estado_equipo_form = EstadoForm(request.POST, instance = estado)
        if estado_equipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            estado_equipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_estado_equipo',{'estado_equipo_form':estado_equipo_form,'estadoEquipo':estadoEquipo,'estado':estado})    #redireccionar al index  
    return render(request,'Servicios/editar_estado_equipo.html',{'estado_equipo_form':estado_equipo_form,'estadoEquipo':estadoEquipo,'estado':estado})

#Eliminar un Estado de Equipo
def eliminarEstadoEquipo (request,id):
    estadoEquipo = Estado.objects.all()
    estado_equipo_form=None
    try:
        #estadoE = get_object_or_404(Estado,id=id)
        estadoE = Estado.objects.get(id = id) 
        estadoE.delete()
        messages.warning(request, 'Se eliminó el estado de equipo')
        return redirect('/Servicios/crear_estado_equipo',{'estado_equipo_form' : estado_equipo_form, 'estadoEquipo':estadoEquipo})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el estado de equipo')
    return render(request, 'Servicios/listar_estado_equipo.html',{'estado_equipo_form' : estado_equipo_form, 'estadoEquipo':estadoEquipo})


#listar Estado Equipo
def listarEstadoEquipo(request):
    estadoEquipo = Estado.objects.all()
    return render(request,'Servicios/listar_estado_equipo.html',{'estadoEquipo':estadoEquipo})
################################################################################################################


############################################### Estado de Repuesto ###################################################

#crear Estado de Repuesto
def crearEstadoRepuesto(request):
    estadoRepuesto = Estado_Repuesto.objects.all()
    if request.method == 'POST':
        estado_repuesto_form = Estado_RepuestoForm(request.POST) #recibe todos los datos del formulario
        if estado_repuesto_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            estado_repuesto_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            print('Ocurrió un error al tratar de crear el equipo')
            return redirect('/Servicios/crear_estado_repuesto')    #redireccionar al index
    else:
        estado_repuesto_form = Estado_RepuestoForm()
    return render(request,'Servicios/crear_estado_repuesto.html',{'estado_repuesto_form':estado_repuesto_form,'estadoRepuesto':estadoRepuesto})

#Editar un Estado de Repuesto
def editarEstadoRepuesto(request,id):
    estadoRepuesto = Estado_Repuesto.objects.all()
    estado_repuesto_form = None 
    estadoR = Estado_Repuesto.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        estado_repuesto_form = MarcaForm(instance = estadoR)       #ver de que es este instance = ??????????????????????????
    else:
        estado_repuesto_form = MarcaForm(request.POST, instance = estadoR)
        if estado_repuesto_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            estado_repuesto_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/listar_estado_repuesto',{'estado_repuesto_form':estado_repuesto_form,'estadoRepuesto':estadoRepuesto,'estadoR':estadoR})    #redireccionar al index    
    return render(request,'Servicios/editar_estado_repuesto.html',{'estado_repuesto_form':estado_repuesto_form,'estadoRepuesto':estadoRepuesto,'estadoR':estadoR})

#Eliminar un Estado de Repuesto
def eliminarEstadoRepuesto (request,id):
    estadoRepuesto = Estado_Repuesto.objects.all()
    estado_repuesto_form=None
    try:
        estadoR = Estado_Repuesto.objects.get(id = id)
        estadoR.delete()
        return redirect('/Servicios/crear_estado_repuesto',{'estado_repuesto_form' : estado_repuesto_form, 'estadoRepuesto':estadoRepuesto})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el país')
    return render(request, 'Servicios/listar_estado_repuesto.html',{'estado_repuesto_form' : estado_repuesto_form, 'estadoRepuesto':estadoRepuesto})

#listar Estado de Repuesto
def listarEstadoRepuesto(request):
    estadoRepuesto = Estado_Repuesto.objects.all()
    return render(request,'Servicios/listar_estado_repuesto.html',{'estadoRepuesto':estadoRepuesto})

################################################################################################################

############################################### Tipo de Memoria ###################################################
#Crear Tipo Memoria
def crearTipoMemoria(request):
    tipo_Memoria = TipoMemoria.objects.all()
    if request.method == 'POST':
        tipoMemoria_form = TipoMemoriaForm(request.POST) #recibe todos los datos del formulario
        if tipoMemoria_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoMemoria_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_tipo_memoria')    #redireccionar al index
    else:
        tipoMemoria_form = TipoMemoriaForm()
    return render(request,'Servicios/crear_tipo_memoria.html',{'tipoMemoria_form':tipoMemoria_form,'tipo_Memoria':tipo_Memoria})


#Editar Tipo Memoria
def editarTipoMemoria(request,id):
    tipo_Memoria = TipoMemoria.objects.all()
    tipoMemoria_form = None 
    tipo = TipoMemoria.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        tipoMemoria_form = TipoMemoriaForm(instance = tipo)       #ver de que es este instance = ??????????????????????????
    else:
        tipoMemoria_form = TipoMemoriaForm(request.POST, instance = tipo)
        if tipoMemoria_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoMemoria_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_tipo_memoria',{'tipoMemoria_form':tipoMemoria_form,'tipo_Memoria':tipo_Memoria,'tipo':tipo})    #redireccionar al index
    return render(request,'Servicios/editar_tipo_memoria.html',{'tipoMemoria_form':tipoMemoria_form,'tipo_Memoria':tipo_Memoria,'tipo':tipo})


#eliminar Tipo Memoria
def eliminarTipoMemoria (request,id):
    tipo_Memoria = TipoMemoria.objects.all()
    tipoMemoria_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        tipoM = TipoMemoria.objects.get(id = id) 
        tipoM.delete()
        return redirect('/Servicios/crear_tipo_memoria',{'tipoMemoria_form' : tipoMemoria_form, 'tipo_Memoria':tipo_Memoria})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de equipo ya que tiene equipos asociados')
    return render(request, 'Servicios/listar_tipo_memoria.html',{'tipoMemoria_form' : tipoMemoria_form, 'tipo_Memoria':tipo_Memoria})


#listar Tipo Memoria
def listarTipoMemoria(request):
    tipo_Memoria = TipoMemoria.objects.all()
    return render(request,'Servicios/listar_tipo_memoria.html',{'tipo_Memoria':tipo_Memoria})
################################################################################################################

############################################### Tipo de Discco ###################################################
#Crear Tipo Disco
def crearTipoDisco(request):
    tipo_Disco = TipoDisco.objects.all()
    if request.method == 'POST':
        tipoDisco_form = TipoDiscoForm(request.POST) #recibe todos los datos del formulario
        if tipoDisco_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoDisco_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_tipo_disco')    #redireccionar al index
    else:
        tipoDisco_form = TipoDiscoForm()
    return render(request,'Servicios/crear_tipo_disco.html',{'tipoDisco_form':tipoDisco_form,'tipo_Disco':tipo_Disco})


#Editar Tipo Disco
def editarTipoDisco(request,id):
    tipo_Disco = TipoDisco.objects.all()
    tipoDisco_form = None 
    tipo = TipoDisco.objects.get(id = id) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        tipoDisco_form = TipoDiscoForm(instance = tipo)       #ver de que es este instance = ??????????????????????????
    else:
        tipoDisco_form = TipoDiscoForm(request.POST, instance = tipo)
        if tipoDisco_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoDisco_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_tipo_disco',{'tipoDisco_form':tipoDisco_form,'tipo_Disco':tipo_Disco,'tipo':tipo})    #redireccionar al index
    return render(request,'Servicios/editar_tipo_disco.html',{'tipoDisco_form':tipoDisco_form,'tipo_Disco':tipo_Disco,'tipo':tipo})


#eliminar Tipo Disco
def eliminarTipoDisco (request,id):
    tipo_Disco = TipoDisco.objects.all()
    tipoDisco_form=None
    try:
        #marca = get_object_or_404(Marca,id=id)
        tipoD = TipoDisco.objects.get(id = id) 
        tipoD.delete()
        return redirect('/Servicios/crear_tipo_disco',{'tipoDisco_form' : tipoDisco_form, 'tipo_Disco':tipo_Disco})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar el tipo de disco ya que tiene equipos asociados')
    return render(request, 'Servicios/listar_tipo_disco.html',{'tipoDisco_form' : tipoDisco_form, 'tipo_Disco':tipo_Disco})


#listar Tipo Disco
def listarTipoDisco(request):
    tipo_Disco = TipoDisco.objects.all()
    return render(request,'Servicios/listar_tipo_disco.html',{'tipo_Disco':tipo_Disco})
################################################################################################################
