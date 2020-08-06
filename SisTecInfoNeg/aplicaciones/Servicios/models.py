from django.db import models
from aplicaciones.Personas.models import *
#from aplicaciones.Personas.models import Usuario

from django.core.validators import MinValueValidator

class TipoEquipo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del tipo de equipo', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'TipoEquipo'
        verbose_name_plural = 'TipoEquipo'
    
    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(TipoEquipo, self).save(*args, **kwargs)

class Estado(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Estado del equipo', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estado'
    
    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Estado, self).save(*args, **kwargs)

class Marca(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Marca del equipo', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'
    
    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Marca, self).save(*args, **kwargs)

class Servicio_Tecnico(models.Model):
    codServicio = models.AutoField('Codigo de Servicio', primary_key = True, null = False, blank = False)
    fechaIngreso = models.DateField('Fecha de Ingreso', null = False, blank = False)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)
    tipoEquipo = models.ForeignKey(TipoEquipo, on_delete = models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete = models.PROTECT)
    modelo = models.CharField('Modelo del equipo', max_length = 100, null = False, blank = False)
    problema = models.CharField('Descripcion del problema', max_length = 200, null = False, blank = False)
    contraseña = models.CharField('Contraseña del equipo', max_length = 100, null = False, blank = False)
    cargador = models.BooleanField(default = False)
    fechaEntrega = models.DateField('Fecha de Entrega', null = False, blank = False)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    trabajosRealizados = models.CharField('Trabajos realizados sobre el equipo', max_length = 200, null = False, blank = False)
    ubicacion = models.CharField('Ubicacion o Estante en el que se encuentra', max_length = 200, null = False, blank = False)
    cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    
    #repuesto = models.ForeignKey(Repuesto, on_delete = models.PROTECT)

    class Meta:
        verbose_name = 'Servicio_Tecnico'
        verbose_name_plural = 'Servicios_Tecnicos'
        ordering = ['codServicio']

    def __str__(self):
        return str(self.codServicio)

class Estado_Repuesto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Estado del equipo', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Estado_Repuesto'
        verbose_name_plural = 'Estado_Repuesto'
    
    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Estado_Repuesto, self).save(*args, **kwargs)

class Repuesto(models.Model):
    codRepuesto = models.PositiveIntegerField('Codigo de Repuesto', primary_key = True, null = False, blank = False)
    nombre = models.CharField('Nombre del Repuesto', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripcion del Repuesto', max_length = 200, null = False, blank = False)
    estado = models.ForeignKey(Estado_Repuesto, on_delete = models.PROTECT)
    stock = models.PositiveIntegerField()
    servicio = models.ForeignKey(Servicio_Tecnico, on_delete = models.PROTECT,null = True, blank = True)
    entrega = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, default = 0, validators=[MinValueValidator(0.00)])


    class Meta:
        verbose_name = 'Repuesto'
        verbose_name_plural = 'Repuestos'
        ordering = ['nombre']
    
    def __str__(self):
        return str(self.nombre)
