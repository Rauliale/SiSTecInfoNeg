#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from aplicaciones.Servicios.forms import Servicio_TecnicoForm
from aplicaciones.Servicios.models import Servicio_Tecnico
#from aplicaciones.mixins import ValidatePermissionRequiredMixin


def servicios_list(request):
    data = {
        'title': 'Listado de Servicios Pendientes',
        'servicios': Servicio_Tecnico.objects.all()
    }
    return render(request, 'pila_de_trabajo/list.html', data)


class ServiciosListView(ListView):       #LoginRequiredMixin, ValidatePermissionRequiredMixin, 
    model = Servicio_Tecnico
    template_name = 'pila_de_trabajo/list.html'
    #permission_required = 'carreras.view_materias'
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Servicio_Tecnico.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Servicios'
        context['create_url'] = reverse_lazy('Servicios:pila_de_trabajo_create')
        context['list_url'] = reverse_lazy('Servicios:pila_de_trabajo_list')
        context['entity'] = 'Servicio_Tecnico'
        return context

class ServiciosCreateView(CreateView): #LoginRequiredMixin, ValidatePermissionRequiredMixin, 
    model = Servicio_Tecnico
    form_class = Servicio_TecnicoForm
    template_name = 'pila_de_trabajo/create.html'
    success_url = reverse_lazy('Stock:pila_de_trabajo_list')
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
            if action == 'search_servicio_id':
                servicio = Servicio_Tecnico.objects.get(pk=request.POST['id'])
                data = [{'id': '', 'text': '---------'}]
                #for i in AnioCursado.objects.filter(nombre=request.POST['id']):
                #for i in AnioCursado.objects.filter(nombre__gte=1, nombre__lte=anios):
                #    data.append({'id': i.id, 'text': i.nombre})
            elif action == 'add':
                form = Servicio_TecnicoForm(request.POST)
                if form.is_valid():
                    print("entro al formulario para guardarlo")
                    form = self.get_form()
                    data = form.save()
                return redirect('Stock:pila_de_servicios_list')
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Servicio'
        context['entity'] = 'Servicio_Tecnico'
        context['list_url'] = reverse_lazy('Stock:pila_de_trabajo_list')
        context['action'] = 'add'
        return context


