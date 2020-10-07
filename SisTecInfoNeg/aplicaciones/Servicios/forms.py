from django import forms
from .models import *

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['unidad','cantidad'] 
        widgets = {
        'unidad' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Unidad', 'style' : 'margin-bottom:2px;'}),
        'cantidad' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Cantidad', 'style' : 'margin-bottom:2px;'}),
        }


class TipoComponenteForm(forms.ModelForm):
    class Meta:
        model = TipoComponente
        fields = ['tipo']
        widgets = {
        'tipo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Tipo de Componente', 'style' : 'margin-bottom:2px;'}),
        }

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['nombre','tipoComponente','unidad']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Componente', 'style' : 'margin-bottom:2px;'}),
        'unidad' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'tipoComponente' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
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
        fields = ['cliente','tipoEquipo','marca','modelo','componente']
        widgets = {
        'cliente': forms.Select(attrs={'id':'comboCliente','class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'tipoEquipo' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'marca' : forms.Select(attrs={'id':'comboMarca','class' : 'js-example-basic-single form-control form-control-user', 'style':'width: 100%'}),
        'modelo' : forms.TextInput(attrs={'id':'textModelo','type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Modelo', 'style' : 'margin-bottom:2px;'}),
        'componente': forms.SelectMultiple(attrs={'class': "js-example-basic-multiple", 'multiple':'multiple'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','slug','descripcion','contenido','url1','url2','url3','imagen','autor','categoria','estado',]

class Servicio_TecnicoForm(forms.ModelForm):
    class Meta:
        model = Servicio_Tecnico
        fields = ['fechaIngreso','fechaEntrega','estado','problema','contraseña','accesorio','ubicacion','equipo','trabajosRealizados','presupuesto','prioridad']
        widgets = {
        'fechaIngreso' : forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm', 'style':'width: 100%'}),   
        'fechaEntrega' : forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm', 'style':'width: 100%'}),   
        'estado' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'problema' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Problema', 'style' :'width: 100%;','style':'height:70px'}),
        'contraseña' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Contraseña', 'style':'width: 100%'}),
        'ubicacion' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Ubicacion en donde se guarda en quipo', 'style':'width: 100%'}),
        'equipo' : forms.Select(attrs={'id': 'comboEquipo' ,'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'accesorio' : forms.SelectMultiple(attrs={'class': "js-example-basic-multiple", 'multiple':'multiple', 'placeholder' : 'Seleccione accesorios'}),
        'trabajosRealizados' : forms.Textarea(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Problema', 'style':'width: 100%','style':'height:70px'}),
        'presupuesto' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Pesupuesto', 'style':'width: 100%'}),        
        'prioridad': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        }

    
class Estado_RepuestoForm(forms.ModelForm):
    class Meta:
        model = Estado_Repuesto
        fields = ['nombre']

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['nombre','descripcion','estado','stock','servicio','entrega']

