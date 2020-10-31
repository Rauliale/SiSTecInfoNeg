#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from aplicaciones.Stock.forms import MovimientoForm
from aplicaciones.Stock.models import Movimiento
#from aplicaciones.mixins import ValidatePermissionRequiredMixin


def movimientos_list(request):
    data = {
        'title': 'Listado de Movimientos',
        'movimientos': Movimiento.objects.all()
    }
    return render(request, 'movimiento/list.html', data)


class MovimientoListView(ListView):       #LoginRequiredMixin, ValidatePermissionRequiredMixin, 
    model = Movimiento
    template_name = 'movimiento/list.html'
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
                for i in Movimiento.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Movimientos'
        context['create_url'] = reverse_lazy('Stock:movimiento_create')
        context['list_url'] = reverse_lazy('Stock:movimiento_list')
        context['entity'] = 'Movimiento'
        return context



class MovimientoCreateView(CreateView): #LoginRequiredMixin, ValidatePermissionRequiredMixin, 
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/create.html'
    success_url = reverse_lazy('Stock:movimiento_list')
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
            if action == 'search_movimiento_id':
                movimiento = Movimiento.objects.get(pk=request.POST['id'])
                data = [{'id': '', 'text': '---------'}]
                #for i in AnioCursado.objects.filter(nombre=request.POST['id']):
                #for i in AnioCursado.objects.filter(nombre__gte=1, nombre__lte=anios):
                #    data.append({'id': i.id, 'text': i.nombre})
            elif action == 'add':
                form = MovimientoForm(request.POST)
                if form.is_valid():
                    print("entro al formulario para guardarlo")
                    form = self.get_form()
                    data = form.save()
                return redirect('Stock:movimiento_list')
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear un Movimiento'
        context['entity'] = 'Movimiento'
        context['list_url'] = reverse_lazy('Stock:movimiento_list')
        context['action'] = 'add'
        return context


class MovimientoUpdateView(UpdateView):           #LoginRequiredMixin, ValidatePermissionRequiredMixin, 
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'movimiento/create.html'
    success_url = reverse_lazy('Stock:movimiento_list')
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
                return redirect('Stock:movimiento_list')
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Movimiento'
        context['entity'] = 'Movimiento'
        context['list_url'] = reverse_lazy('Stock:movimiento_list')
        context['action'] = 'edit'
        return context

class MovimientoDeleteView( DeleteView):      #LoginRequiredMixin, ValidatePermissionRequiredMixin,
    model = Movimiento
    template_name = 'movimiento/delete.html'
    success_url = reverse_lazy('movimiento:movimiento_list')
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
        context['title'] = 'Eliminar Movimiento'
        context['entity'] = 'Movimiento'
        context['list_url'] = reverse_lazy('movimiento:movimiento_list')
        return context