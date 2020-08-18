from django import forms
from .models import *


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['provincia']
        widgets = {
        'provincia' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Provincia', 'style' : 'margin-bottom:2px;'}),
        }

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = ['localidad','provincia']
        widgets = {
        'localidad' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        'provincia' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        }

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ['calle','nro','mz','departamento','piso']
        widgets = {
        'calle' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Calle', 'style' : 'margin-bottom:2px;'}),
        'nro' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Numero', 'style' : 'margin-bottom:2px;'}),
        'mz' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Manzana', 'style' : 'margin-bottom:2px;'}),
        'departamento' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Departamento', 'style' : 'margin-bottom:2px;'}),
        'piso' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Piso', 'style' : 'margin-bottom:2px;'}),
        
        }

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['prefijo','numero','whatsapp','tipo_telefono']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['dni','nombre','apellido','fechaNac','sexo','domicilio','telefono','correoElectronico']

class ClienteForm(UsuarioForm.Meta):
    class Meta:
        model = Cliente
        fields = ['nombreEmpresa'] #'dni','nombre','apellido','fechaNac','sexo','domicilio','telefono','correoElectronico',
        widgets = {
        #'dni' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'apellido' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'fechaNac' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'sexo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'domicilio' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'telefono' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        #'correoElectronico' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        'nombreEmpresa' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Localidad', 'style' : 'margin-bottom:2px;'}),
        }
class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre','descripcion']

class TecnicoForm(UsuarioForm.Meta):
    class Meta:
        model = Tecnico
        fields = ['turno','especialidades']

class EmpleadoForm(UsuarioForm.Meta):
    class Meta:
        model = Empleado
        fields = ['turno','puesto']


