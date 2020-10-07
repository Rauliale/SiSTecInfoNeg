from django import forms
from django.forms import ModelForm, TextInput
from .models import *


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Categoria del Articulo', 'style' : 'margin-bottom:2px;'}),
        }

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Categoria del Articulo', 'style' : 'margin-bottom:2px;'}),
        }

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Categoria del Articulo', 'style' : 'margin-bottom:2px;'}),
        }

class TipoMovimientoForm(forms.ModelForm):
    class Meta:
        model = TipoMovimiento
        fields = ['nombre']
        widgets = {
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Tipo de Movimiento', 'style' : 'margin-bottom:2px;'}),
        }

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['tipoMovimiento','tipoComprobante','numeroComprobante','lugar','fechaMovimiento','observaciones','estado','articulo','total']
        widgets = {
        'tipoMovimiento': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'tipoComprobante': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'numeroComprobante' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Numero de comprobante', 'style' : 'margin-bottom:2px;'}),
        'lugar': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'fechaMovimiento' : forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm', 'style':'width: 100%'}),   
        'observaciones' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Observaciones', 'style' : 'margin-bottom:2px;'}),
        'articulo': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'total':forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Total', 'style' : 'margin-bottom:2px;'}),
        
        }

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['categoria','nombreArticulo','grupo','stockMinimo','unidadMedida','estado','precioCompra','precioVenta','cantidad','estado','impuesto','ganancia']
        widgets = {
        'categoria': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'nombreArticulo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Nombre del Articulo', 'style' : 'margin-bottom:2px;'}),
        'grupo': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'stockMinimo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Stock Minimo', 'style':'width: 100%'}),
        'unidadMedida': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'precioCompra': forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Precio de Compra', 'style':'width: 100%'}),
        'precioVenta': forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Precio de Venta', 'style':'width: 100%'}),
        'cantidad':forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-sm', 'placeholder' : 'Stock', 'style':'width: 100%'}),
        'impuesto': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        'ganancia': forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-sm', 'style':'width: 100%'}),
        
        }
        
class ArticuloForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = Articulo
        fields = '__all__'
        widgets = {
            'nombreArticulo': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del Articulo',
                }
            ),
            'nombre_corto': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre corto del Articulo (30 caracteres máximo)',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data