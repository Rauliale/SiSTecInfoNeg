from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from datetime import datetime, date, time, timedelta
import calendar



class Turno(models.Model):
    id_turno=models.AutoField(primary_key=True)
    turno=models.CharField('Turno', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.turno

class Provincia(models.Model):
    id_provincia=models.AutoField(primary_key=True)
    provincia=models.CharField('Provincia', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.provincia

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key = True)
    localidad=models.CharField('Localidad', max_length=50,blank=False,null=False)
    provincia=models.ForeignKey(Provincia,on_delete=models.PROTECT)
    borrado = models.BooleanField('borrado',default=False)
    def __str__(self):
        return self.localidad

class Domicilio(models.Model):
    id_domicilio = models.AutoField(primary_key=True)
    calle=models.CharField('Calle', max_length=100,blank=False,null=False)
    nro=models.CharField('Numero', max_length=50,blank=False,null=False)
    mz = models.CharField('Manzana', max_length=50,null=True,blank=True)
    departamento=models.CharField('Departamento', max_length=50,null=True,blank=True)
    piso=models.CharField('Piso', max_length=50,null=True,blank=True)
    borrado = models.BooleanField('borrado',default=False)
    
    def __str__(self):
        return 'calle '+ self.calle + ' - ' + str(self.nro)

class Tipo_Telefono(models.Model):
    TIPO={
        ('Movil','Movil'),
        ('Fijo','Fijo')
    }
    EMPRESA={
        ('Personal','Personal'),
        ('Claro','Claro'),
        ('Movistar','Movistar'),
        ('Tuenti','Tuenti'),
        ('Otro','Otro')
    }
    id_tipo_telefono=models.AutoField(primary_key=True)
    tipo=models.CharField('Tipo', max_length=50,blank=True,null=True,choices=TIPO)
    empresa=models.CharField('Empresa', max_length=50,blank=True,null=True,choices=EMPRESA)
    borrado = models.BooleanField('borrado',default=False)

    
    def __str__(self):
        return self.tipo

class Telefono(models.Model):
    id_telefono=models.AutoField(primary_key=True)
    prefijo=models.IntegerField('Prefijo',blank=True,null=True)
    numero=models.IntegerField('Numero',null=True,blank=True)
    whatsapp=models.BooleanField('Whatsapp',default=True)
    tipo_telefono=models.ForeignKey(Tipo_Telefono, on_delete=models.PROTECT,null=True)
    borrado = models.BooleanField('borrado',default=False)    
    # miembro no def :C contacto= models.ForeignKey(Miembro, on_delete=models.PROTECT,null=True) #tel de contacto en caso de necesitar
    
    def __str__(self):
        return str(self.prefijo) + ' - ' + str(self.numero) 



class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del rol', max_length = 100, null = False, blank = False)
    descripcion = models.TextField('Descripcion del rol', null = True, blank = True)
    

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.descripcion = (self.descripcion).upper()
        return super(Rol, self).save(*args, **kwargs)

   
class Cliente(models.Model):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    nombreEmpresa = models.TextField('Empresa del cliente', null = True, blank = True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        permissions = (("es_cliente", "es cliente"),("es_pre_cliente", "es pre cliente"))

    def __str__(self):
            return str(self.nombre) + ' ' + str(self.apellido )
            #return self.apellido

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.apellido = (self.apellido).upper()
        self.domicilio = (self.domicilio)        
        return super(Cliente, self).save(*args, **kwargs)



class Especialidad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la especialidad', max_length = 100, null = False, blank = False)
    descripcion = models.TextField('Descripcion de la especialidad', null = False, blank = False)
    estadoEsp = models.BooleanField('activo/inactivo', default = True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        


    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.descripcion = (self.descripcion).upper()
        return super(Especialidad, self).save(*args, **kwargs)

class Tecnico(models.Model):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    turno = models.ManyToManyField(Turno, blank = True)
    especialidades = models.ManyToManyField(Especialidad, blank = True)

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        permissions = (("es_Tecnico", "es Tecnico"),("es_pre_Tecnico", "es pre Tecnico"))

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre
        #return self.apellido
class Empleado(models.Model):
    dni = models.PositiveIntegerField('DNI', primary_key = True, null = False, blank = False)
    rol = models.ForeignKey(Rol, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombre = models.CharField('Nombre del usuario', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del usuario', max_length = 200, null = False, blank = False)
    fechaNac = models.DateField('Fecha de Nacimiento', null = False, blank = False)
    sexo = models.CharField('Sexo de la persona', max_length = 50, null = False, blank = False)
    domicilio=models.ForeignKey(Domicilio, on_delete=models.PROTECT)
    telefono=models.ForeignKey(Telefono, on_delete=models.PROTECT,null=True)
    correoElectronico = models.EmailField('Correo electronico del usuario', null =  False, blank = False)
    estado = models.BooleanField('Usuario activo/inactivo', default = False)
    turno = models.ManyToManyField(Turno, blank = True)
    puesto = models.CharField('Puesto de trabajo del Empleado', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        permissions = (("es_Empleado", "es Empleado"),("es_pre_Empleado", "es pre Empleado"))

    def __str__(self):
        return str(self.dni) + ' - ' + self.apellido + ' ' + self.nombre
        #return self.apellido

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        self.apellido = (self.apellido).upper()
        self.domicilio = (self.domicilio)        
        return super(Empleado, self).save(*args, **kwargs)