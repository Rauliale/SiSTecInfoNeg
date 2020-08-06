from django import forms
from .models import TipoEquipo,Estado,Marca,Servicio_Tecnico,Estado_Repuesto,Repuesto


class TipoEquipoForm(forms.ModelForm):
    class Meta:
        model = TipoEquipo
        fields = ['nombre']

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class Servicio_TecnicoForm(forms.ModelForm):
    class Meta:
        model = Servicio_Tecnico
        fields = ['fechaIngreso','estado','tipoEquipo','marca','modelo','problema','contraseña','cargador','fechaEntrega','presupuesto','trabajosRealizados','ubicacion','cliente']
    
class Estado_RepuestoForm(forms.ModelForm):
    class Meta:
        model = Estado_Repuesto
        fields = ['nombre']

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre','descripcion','estado','stock','servicio','entrega']