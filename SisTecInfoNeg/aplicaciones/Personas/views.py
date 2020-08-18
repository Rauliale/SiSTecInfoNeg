from django.shortcuts import render, redirect
from .forms import *
from .models import *

from django.contrib import messages
# Create your views here.

#################################################### Provincia ##############################################################
#Crear Provincia
def crearProvincia(request):
    provincia = Provincia.objects.all()
    if request.method == 'POST':
        provincia_form = ProvinciaForm(request.POST) #recibe todos los datos del formulario
        print(provincia_form.errors)
        if provincia_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            provincia_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear la provincia')
            return redirect('index')    #redireccionar para volver a cargar otro servicio
    
    else:
        provincia_form = ProvinciaForm()
    return render(request,'Personas/crear_provincia.html',{'provincia_form':provincia_form,'provincia':provincia})

#Editar Privincia
def editarProvincia(request,id_provincia):
    provincia = Provincia.objects.all()
    provincia_form = None 
    prov = Provincia.objects.get(id_provincia = id_provincia) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        provincia_form = ProvinciaForm(instance = prov)      
    else:
        provincia_form = ProvinciaForm(request.POST, instance = prov)
        if provincia_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            provincia_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Personas/listar_provincia',{'provincia_form':provincia_form,'provincia':provincia,'prov':prov})    
    return render(request,'Personas/editar_provincia.html',{'provincia_form':provincia_form,'provincia':provincia,'prov':prov})

#Eliminar una Provincia
def eliminarProvincia (request,id_provincia):
    provincia = Provincia.objects.all()
    provincia_form=None
    try:
        prov = Provincia.objects.get(id_provincia = id_provincia) 
        prov.delete()
        return redirect('/Personas/crear_provincia',{'provincia_form' : provincia_form, 'provincia':provincia})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la marca ya que tiene equipos asociados')
        print('entro acá 2')#no está mandando el error al front end
    return render(request, 'Personas/listar_provincia.html',{'provincia_form' : provincia_form, 'provincia':provincia})



#listar Provincia
def listarProvincia(request):
    provincia = Provincia.objects.all()
    return render(request,'Personas/listar_provincia.html',{'provincia':provincia})

##################################################################################################################

#################################################### Localidades ####################################################

#Crear Localidades
def crearLocalidad(request):
    localidad = Localidad.objects.all()
    if request.method == 'POST':
        localidad_form = LocalidadForm(request.POST) #recibe todos los datos del formulario
        print(localidad_form.errors)
        if localidad_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            localidad_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear la localidad')
            return redirect('index')    #redireccionar para volver a cargar otro servicio
    
    else:
        localidad_form = LocalidadForm()
    return render(request,'Personas/crear_localidad.html',{'localidad_form':localidad_form,'localidad':localidad})

#Editar Localidad
def editarLocalidad(request,id_localidad):
    localidad = Localidad.objects.all()
    localidad_form = None 
    loc = Localidad.objects.get(id_localidad = id_localidad) #aca tengo que cambiar mi variable tipo_Equipo con otro nombre
    if request.method == 'GET':
        localidad_form = LocalidadForm(instance = loc)      
    else:
        localidad_form = LocalidadForm(request.POST, instance = loc)
        if localidad_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            localidad_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('/Personas/listar_localidad',{'localidad_form':localidad_form,'localidad':localidad,'loc':loc})    
    return render(request,'Personas/editar_localidad.html',{'localidad_form':localidad_form,'localidad':localidad,'loc':loc})

#Eliminar una Localidad
def eliminarLocalidad(request,id_localidad):
    localidad = Localidad.objects.all()
    localidad_form=None
    try:
        loc = Localidad.objects.get(id_localidad = id_localidad) 
        loc.delete()
        return redirect('/Personas/crear_localidad',{'localidad_form' : localidad_form, 'localidad':localidad})
    except Exception as e:
        messages.error(request, 'Ocurrió un error al tratar de eliminar la marca ya que tiene equipos asociados')
        print('entro acá 2')#no está mandando el error al front end
    return render(request, 'Personas/listar_localidad.html',{'localidad_form' : localidad_form, 'localidad':localidad})


#listar Localidades
def listarLocalidad(request):
    localidad = Localidad.objects.all()
    return render(request,'Personas/listar_localidad.html',{'localidad':localidad})
##################################################################################################################

#################################################### Clientes ####################################################

#Crear Clientes
def crearCliente(request):
    cliente = Cliente.objects.all()
    #usuario = Usuario.objects.all()
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST) #recibe todos los datos del formulario
        usuario_form = UsuarioForm(request.POST) #recibe todos los datos del formulario
        print(cliente_form.errors)
        if cliente_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            cliente_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear la cliente')
            return redirect('index')    #redireccionar para volver a cargar otro servicio
    
    else:
        cliente_form = ClienteForm()
        usuario_form = UsuarioForm()
    return render(request,'Personas/crear_cliente.html',{'cliente_form':cliente_form,'usuario_form':usuario_form,'cliente':cliente}) #,'usuario':usuario


#listar Clientes
def listarCliente(request):
    cliente = Cliente.objects.all()
    return render(request,'Personas/listar_cliente.html',{'cliente':cliente})
##################################################################################################################

#################################################### Tecnico ####################################################

#Crear Tecnico
def crearTecnico(request):
    tecnico = Tecnico.objects.all()
    #usuario = Usuario.objects.all()
    if request.method == 'POST':
        tecnico_form = TecnicoForm(request.POST) #recibe todos los datos del formulario
        usuario_form = UsuarioForm(request.POST) #recibe todos los datos del formulario
        print(tecnico_form.errors)
        if tecnico_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tecnico_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear la tecnico')
            return redirect('index')    #redireccionar para volver a cargar otro servicio
    
    else:
        tecnico_form = TecnicoForm()
        usuario_form = UsuarioForm()
    return render(request,'Personas/crear_tecnico.html',{'tecnico_form':tecnico_form,'usuario_form':usuario_form,'tecnico':tecnico}) #,'usuario':usuario


#listar tecnico
def listarTecnico(request):
    tecnico = Tecnico.objects.all()
    return render(request,'Personas/listar_tecnico.html',{'tecnico':tecnico})
##################################################################################################################

#################################################### Empleado ####################################################

#Crear Empleado
def crearEmpleado(request):
    empleado = Empleado.objects.all()
    #usuario = Usuario.objects.all()
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST) #recibe todos los datos del formulario
        usuario_form = UsuarioForm(request.POST) #recibe todos los datos del formulario
        print(empleado_form.errors)
        if empleado_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            empleado_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear la empleado')
            return redirect('index')    #redireccionar para volver a cargar otro servicio
    
    else:
        empleado_form = EmpleadoForm()
        usuario_form = UsuarioForm()
    return render(request,'Personas/crear_empleado.html',{'empleado_form':empleado_form,'usuario_form':usuario_form,'empleado':empleado}) #,'usuario':usuario


#listar Empleado
def listarEmpleado(request):
    empleado = Empleado.objects.all()
    return render(request,'Personas/listar_empleado.html',{'empleado':empleado})
##################################################################################################################