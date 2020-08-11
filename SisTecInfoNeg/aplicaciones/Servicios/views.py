from django.shortcuts import render, redirect
from .forms import *
from .models import Servicio_Tecnico,Marca,TipoEquipo
# Create your views here.

def Home(request):
    return render(request, 'index.html')


def crearServicio(request):
    servicios = Servicio_Tecnico.objects.all()
    if request.method == 'POST':
        servicio_form = Servicio_TecnicoForm(request.POST) #recibe todos los datos del formulario
        print(servicio_form.errors)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:
            print('Ocurrió un error al tratar de crear el Servicio Tecnico')
            #return redirect('index')    #redireccionar al index
    
    else:
        servicio_form = Servicio_TecnicoForm()
    return render(request,'Servicios/crear_servicio.html',{'servicio_form':servicio_form,'servicios':servicios})

#def listarServicio(request):
    #servicios = Servicio_Tecnico.objects.all()
    #return render(request,'Servicios/listar_servicio.html',{'servicios':servicios})

def editarServicio(request,codServicio):
    servicios = Servicio_Tecnico.objects.all()
    servicio_form = None 
    servicio = Servicio_Tecnico.objects.get(codServicio = codServicio)
    if request.method == 'GET':
        servicio_form = Servicio_TecnicoForm(instance = servicio)
    else:
        servicio_form = Servicio_TecnicoForm(request.POST, instance = servicio)
        if servicio_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            servicio_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('Servicios/crear_servicio',{'servicio_form':servicio_form,'servicios':servicios})    #redireccionar al index
    return render(request,'Servicios/crear_servicio.html',{'servicio_form':servicio_form,'servicios':servicios})



def crearMarca(request):
    if request.method == 'POST':
        marca_form = MarcaForm(request.POST) #recibe todos los datos del formulario
        if marca_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            marca_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('index')    #redireccionar al index
    else:
        marca_form = MarcaForm()
    return render(request,'Servicios/crear_marca.html',{'marca_form':marca_form})

def listarMarcas(request):
    marcas = Marca.objects.all()
    return render(request,'Servicios/listar_marcas.html',{'marcas':marcas})

def crearTipoEquipo(request):
    tipo_Equipo = TipoEquipo.objects.all()
    if request.method == 'POST':
        tipoEquipo_form = TipoEquipoForm(request.POST) #recibe todos los datos del formulario
        print(tipoEquipo_form.errors)
        if tipoEquipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoEquipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
        else:    
            print('Ocurrió un error al tratar de crear el Servicio Tecnico')
            #return redirect('index')    #redireccionar al index
    else:
        tipoEquipo_form = TipoEquipoForm()
    return render(request,'Servicios/crear_tipo_equipo.html',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo})

def editarTipoEquipo(request,codServicio):
    tipo_Equipo = TipoEquipo.objects.all()
    tipoEquipo_form = None 
    tipo_Equipo = TipoEquipo.objects.get(codServicio = codServicio)
    if request.method == 'GET':
        tipoEquipo_form = TipoEquipoForm(instance = servicio)
    else:
        tipoEquipo_form = TipoEquipoForm(request.POST, instance = servicio)
        if tipoEquipo_form.is_valid():    #is_valid es una funcion de django que valida todos los campos
            tipoEquipo_form.save()        #guardar o registrar en la base de datos lo que esta en el formullario
            return redirect('Servicios/crear_servicio',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo})    #redireccionar al index
    return render(request,'Servicios/crear_servicio.html',{'tipoEquipo_form':tipoEquipo_form,'tipo_Equipo':tipo_Equipo})




#def listarTipoEquipo(request):
#    tipoEquipo = TipoEquipo.objects.all()
#    return render(request,'Servicios/listar_tipo_equipo.html',{'tipoEquipo':tipoEquipo})

