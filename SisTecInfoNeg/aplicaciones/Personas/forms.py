from django import forms
from .models import *


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

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombreEmpresa','dni','nombre','apellido','fechaNac','sexo','domicilio','telefono','correoElectronico']
        widgets = {
        'dni' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'DNI', 'style' : 'margin-bottom:2px;'}),
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Nombre', 'style' : 'margin-bottom:2px;'}),
        'apellido' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Apellido', 'style' : 'margin-bottom:2px;'}),
        'fechaNac' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
        'sexo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Sexo', 'style' : 'margin-bottom:2px;'}),
        'domicilio' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'telefono' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'correoElectronico' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Correo Electronico', 'style' : 'margin-bottom:2px;'}),
        'nombreEmpresa' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Empresa del Cliente', 'style' : 'margin-bottom:2px;'}),
        }


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre','descripcion']

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['turno','especialidades','dni','nombre','apellido','fechaNac','sexo','domicilio','telefono','correoElectronico']
        widgets = {
        'dni' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'DNI', 'style' : 'margin-bottom:2px;'}),
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Nombre', 'style' : 'margin-bottom:2px;'}),
        'apellido' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Apellido', 'style' : 'margin-bottom:2px;'}),
        'fechaNac' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
        'sexo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Sexo', 'style' : 'margin-bottom:2px;'}),
        'domicilio' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'telefono' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'correoElectronico' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Correo Electronico', 'style' : 'margin-bottom:2px;'}),
        'turno': forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Turno', 'style' : 'margin-bottom:2px;'}),
        'especialidades': forms.SelectMultiple() #para ver una lista de cosas cargadas desde una clave foranea
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['turno','puesto','dni','nombre','apellido','fechaNac','sexo','domicilio','telefono','correoElectronico']
        widgets = {
        'dni' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'DNI', 'style' : 'margin-bottom:2px;'}),
        'nombre' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Nombre', 'style' : 'margin-bottom:2px;'}),
        'apellido' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Apellido', 'style' : 'margin-bottom:2px;'}),
        'fechaNac' : forms.DateInput(attrs={'type':'date','class':'form-control'}),
        'sexo' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Sexo', 'style' : 'margin-bottom:2px;'}),
        'domicilio' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'telefono' : forms.Select(attrs={'class' : 'js-example-basic-single form-control form-control-user'}),
        'correoElectronico' : forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Correo Electronico', 'style' : 'margin-bottom:2px;'}),
        'turno': forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Turno', 'style' : 'margin-bottom:2px;'}),
        'puesto': forms.TextInput(attrs={'type' : 'text', 'class' : 'form-control form-control-user', 'placeholder' : 'Puesto', 'style' : 'margin-bottom:2px;'}),
        }


