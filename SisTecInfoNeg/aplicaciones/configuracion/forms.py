from django import forms
from .models import *

class ConfiguracionForm (forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['empresa', 'direccion', 'telefono']