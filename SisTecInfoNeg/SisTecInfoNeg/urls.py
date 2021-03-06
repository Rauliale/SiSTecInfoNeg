"""SisTecInfoNeg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicaciones.Servicios.views import Home
from aplicaciones.login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name = 'index'),
    path('Servicios/',include(('aplicaciones.Servicios.urls','Servicios'))),    #aqui decimos que todas las urls de la aplicacion servicios van an a estar en el tag "Servicios" para poder usar el {% url 'Servicios:elnombredeurldelaAplicacion' %}
    path('Personas/',include(('aplicaciones.Personas.urls','Personas'))),
    path('Stock/',include(('aplicaciones.Stock.urls','Stock'))),
    path('Auditoria/',include(('aplicaciones.Auditoria.urls','Auditoria'))),
    path('login/',include(('aplicaciones.login.urls'))),
]

