from django import forms
from .models import *

class TipoMemoriaForm(forms.ModelForm):
    class Meta:
        model = TipoMemoria
        fields = ['tipo']
        widgets = {
        'tipo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Tipo de Memoria', 'style' : 'margin-bottom:2px;'}),
        }

class CapacidadMemoriaForm(forms.ModelForm):
    class Meta:
        model = CapacidadMemoria
        fields = ['capacidad']
        widgets = {
        'capacidad' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Capacidad de Memoria', 'style' : 'margin-bottom:2px;'}),
        }

class TipoDiscoForm(forms.ModelForm):
    class Meta:
        model = TipoDisco
        fields = ['tipo']
        widgets = {
        'tipo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Tipo de Disco', 'style' : 'margin-bottom:2px;'}),
        }

class CapacidadDiscoForm(forms.ModelForm):
    class Meta:
        model = CapacidadDisco
        fields = ['capacidad']
        widgets = {
        'capacidad' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Capacidad de Disco', 'style' : 'margin-bottom:2px;'}),
        }

class TipoSOForm(forms.ModelForm):
    class Meta:
        model = TipoSO
        fields = ['tipo','version']
        widgets = {
        'tipo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Tipo de Sistema Operativo', 'style' : 'margin-bottom:2px;'}),
        'version' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Version del Sistema Operativo', 'style' : 'margin-bottom:2px;'}),
        }

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['provincia']
        widgets = {
        'provincia' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Provincia', 'style' : 'margin-bottom:2px;'}),
        }


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

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['nombre']
        

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipoEquipo','marca','modelo','cliente','memoria','capacidadMemoria','disco','capacidadDisco','sistemaOperativo']
        widgets = {
        'tipoEquipo' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'marca' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'modelo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Modelo', 'style' : 'margin-bottom:2px;'}),
        'cliente' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'memoria': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'capacidadMemoria': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'disco': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'capacidadDisco': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'sistemaOperativo': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','slug','descripcion','contenido','url1','url2','url3','imagen','autor','categoria','estado',]

class Servicio_TecnicoForm(forms.ModelForm):
    class Meta:
        model = Servicio_Tecnico
        fields = ['fechaIngreso','fechaEntrega','estado','problema','contraseña','accesorio','ubicacion','equipo','trabajosRealizados','presupuesto']
        widgets = {
        'fechaIngreso' : forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm', 'style':'width: 100%'}),   
        'fechaEntrega' : forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm', 'style':'width: 100%'}),   
        'estado' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'problema' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Problema', 'style' :'width: 100%;','style':'height:70px'}),
        'contraseña' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Contraseña', 'style':'width: 100%'}),
        'ubicacion' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Ubicacion en donde se guarda en quipo', 'style':'width: 100%'}),
        'equipo' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'accesorio' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'trabajosRealizados' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Problema', 'style':'width: 100%','style':'height:70px'}),
        'presupuesto' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Pesupuesto', 'style':'width: 100%'}),        
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