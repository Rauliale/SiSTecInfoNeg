from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

from django.contrib import messages

# Create your views here.

#Home
def Home(request):
    return render(request, 'index.html')

def Wiki(request):
    blogs = Blog.objects.filter(estado = True)
    return render(request,'wiki.html',{'blogs':blogs})

############################################################## Servicio Tecnico ###################################################
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





############################################################## Servicio Tecnico ###################################################
#Crear Servicio Tecnico
def crearServicio(request):
    servicios = Servicio_Tecnico.objects.all()
    equipo = Equipo.objects.all()
    if request.method == 'POST':
        servicio_form = Servicio_TecnicoForm(request.POST) #recibe todos los datos del formulario
        equipo_form = EquipoForm(request.POST) #recibe todos los datos del formulario
        print(servicio_form.errors)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Servicios/crear_servicio')    #redireccionar para volver a cargar otro servicio
    else:
        servicio_form = Servicio_TecnicoForm()
        equipo_form = EquipoForm()
    return render(request,'Servicios/crear_servicio.html',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo})

#Editar un Servicio
def editarServicio(request,codServicio):
    servicios = Servicio_Tecnico.objects.all()
    equipo = Equipo.objects.all()
    servicio_form = None
    equipo_form = None
    servicio = Servicio_Tecnico.objects.get(codServicio = codServicio) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    equi = Servicio_Tecnico.Equipo.objects.get(codEquipo = codEquipo)
    if request.method == 'GET':
        servicio_form = Servicio_TecnicoForm(instance = servicio)       #ver de que es este instance = ??????????????????????????
        equipo_form = EquipoForm(instance = equi)
    else:
        servicio_form = Servicio_TecnicoForm(request.POST, instance = servicio)
        equipo_form = EquipoForm(request.POST, instance = equi)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            messages.success(request, 'Se editó correctamente')
            return redirect('/Servicios/listar_servicio',{'servicio_form':servicio_form,'equipo_form':equipo_form,'servicios':servicios,'equipo':equipo})    #redireccionar al index
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
