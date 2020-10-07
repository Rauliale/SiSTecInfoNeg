from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def Configuracion (request):
    
    if request.method == 'POST':
        configuracion_form = ConfiguracionForm(request.POST)
        if configuracion_form.is_valid():
            configuracion = configuracion_form.save()
            messages.success(request, 'Se pudo establecer la configuración correctamente')
        else:
            messages.error(request, 'Ocurrió un error al tratar de establecer la configuración')
    else:
        configuracion_actual = Configuracion.objects.all().last()
        configuracion_form = ConfiguracionForm(instance=configuracion_actual)

    return render(request, 'configuracion/configuracion.html',{'configuracion_form':configuracion_form})

