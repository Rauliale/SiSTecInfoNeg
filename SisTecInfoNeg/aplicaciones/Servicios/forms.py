from django import forms
from .models import *


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

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipoEquipo','marca','modelo','cliente']
        widgets = {
        'tipoEquipo' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'marca' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'modelo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Modelo', 'style' : 'margin-bottom:2px;'}),
        'cliente' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','slug','descripcion','contenido','url1','url2','url3','imagen','autor','categoria','estado',]

class Servicio_TecnicoForm(forms.ModelForm):
    class Meta:
        model = Servicio_Tecnico
        fields = ['fechaIngreso','estado','problema','contraseña','cargador','fechaEntrega','presupuesto','trabajosRealizados','ubicacion','equipo']
        widgets = {
        'fechaIngreso' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Ingrese Fecha de Ingreso', 'style' : 'margin-bottom:10px;'}),   
        'estado' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'problema' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Problema', 'style' : 'margin-bottom:10px;'}),
        'contraseña' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Contraseña', 'style' : 'margin-bottom:10px;'}),
        'fechaEntrega' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Fecha de Entrega', 'style' : 'margin-bottom:2px;'}),
        'presupuesto' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Presupuesto', 'style' : 'margin-bottom:10px;'}),
        'trabajosRealizados' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Trabajos Realizados', 'style' : 'margin-bottom:2px;'}),
        'ubicacion' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Ubicacion en donde se guarda en quipo', 'style' : 'margin-bottom:10px;'}),
        'equipo' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        }
    
    
class Estado_RepuestoForm(forms.ModelForm):
    class Meta:
        model = Estado_Repuesto
        fields = ['nombre']

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre','descripcion','estado','stock','servicio','entrega']

class Tipo_Sistema_OperativoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Sistema_Operativo
        fields = ['sistemaOperativo','version']

class Tipo_DiscoForm(forms.ModelForm):
    class Meta:
        model = Tipo_Disco
        fields = ['disco','capacidad']

class Tipo_MemoriaForm(forms.ModelForm):
    class Meta:
        model = Tipo_Memoria
        fields = ['memoria','capacidad']