
from django.urls import path

from aplicaciones.Auditoria.views import *

urlpatterns = [
    path('audit_serv', audit_serv, name='audit_serv'),
    path('audit_equi', audit_equi, name='audit_equi'),
    

    path('ver_auditoria_servicios/<int:pk>/<int:id_history>', verAuditoriaServicios, name = 'ver_auditoria_servicios'),
    path('ver_auditoria_equipos/<int:pk>/<int:id_history>', verAuditoriaEquipo, name = 'ver_auditoria_equipos'),
    
    path('audit_serv_detail/<int:pk>', audit_serv_detail, name='audit_serv_detail'),
    path('audit_equi_detail/<int:pk>', audit_equi_detail, name='audit_equi_detail'),
    
    path('audit_serv_detail_json/<int:pk>/<int:id_history>', audit_serv_detail_json, name='audit_serv_detail_json'),
    
]