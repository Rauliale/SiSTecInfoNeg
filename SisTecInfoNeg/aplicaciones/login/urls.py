from django.urls import path, include
from aplicaciones.login.views import *

urlpatterns = [
    path('',LoginFormView.as_view(), name = 'login'),
    path('logout/',LogoutRedirectView.as_view(), name = 'logout'),
   
]