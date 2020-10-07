from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import json
from django.http import HttpResponse
from django.http import JsonResponse
from aplicaciones.configuracion.models import Configuracion

#from sayl.utils import get_next_or_prev
from aplicaciones.Servicios.views import Servicio_Tecnico, Equipo
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

###################################### Auditoria Servicios ######################################################
def audit_serv(request):
    audit_servicios = Servicio_Tecnico.history.all()
    reporte = Configuracion.objects.all().last()
    context = {'audit_servicios': audit_servicios,'reporte':reporte}
    return render(request, 'Auditoria/auditoria_servicios.html', context)

#Ver Cambios
def verAuditoriaServicios(request,pk,id_history):
    historial = Servicio_Tecnico.history.filter(codServicio=pk)
    for i in range(len(historial)):
        if historial[i].pk == id_history:
            audit_regsolo = historial[i]
            delta = audit_regsolo.diff_against(historial[i+1])
            data = []
            for change in delta.changes:
                dic = {'change':change.field,'old':change.old, 'new':change.new}
                data.append(dic)
            break
    return JsonResponse(data,safe=False)


def audit_equi(request):
    audit_equipos = Equipo.history.all()
    reporte = Configuracion.objects.all().last()
    context = {'audit_equipos': audit_equipos,'reporte':reporte}
    return render(request, 'Auditoria/auditoria_equipo.html', context)

def audit_equi_detail(request, pk):
    js_historial = Equipo.history.filter(id=pk)    

    context = {'audit_equipos':js_historial, 'detail':True}
    # return render(request, 'auditoria/audit_tjust.html', context)
    return render(request, 'Auditoria/auditoria_Equipo.html', context)


def verAuditoriaEquipo(request,pk,id_history):
    historial = Equipo.history.filter(id=pk)
    for i in range(len(historial)):
        if historial[i].pk == id_history:
            audit_regsolo = historial[i]
            delta = audit_regsolo.diff_against(historial[i+1])
            data = []
            for change in delta.changes:
                dic = {'change':change.field,'old':change.old, 'new':change.new}
                data.append(dic)
            break
    return JsonResponse(data,safe=False)


def audit_serv_detail(request, pk):
    js_historial = Servicio_Tecnico.history.filter(id=pk)    

    context = {'audit_servicios':js_historial, 'detail':True}
    # return render(request, 'auditoria/audit_tjust.html', context)
    return render(request, 'Auditoria/auditoria_servicios.html', context)


def audit_serv_detail_json(request, pk, id_history):
    print(pk, id_history)
    serv_historial = Servicio_Tecnico.history.filter(id=pk)
    historial = Servicio_Tecnico.history.filter(id=pk)
    print(historial)
    if len(serv_historial) > 1:
        for i in range(len(historial)):
            print(id_history, " - ", historial[i].pk)
            if historial[i].pk == id_history:            
                audit_regsolo = historial[i]    
                delta = audit_regsolo.diff_against(serv_historial[i+1])
                print(delta)
                data = []            
                for change in delta.changes:
                    dic = {'change': change.field, 'old':change.old, 'new':change.new}
                    data.append(dic)
                    print("Entro en el for")
                    print(data)
                break
            else:
                data = []
    else:
        data=[{'change':False}]
    print("DATA: ", data)
    return JSONResponse(data)