from django.db import models
from aplicaciones.Personas.models import *
#from aplicaciones.Personas.models import Usuario

from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField

class TipoMemoria(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField('Tipo de Memoria', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.tipo

class CapacidadMemoria(models.Model):
    id=models.AutoField(primary_key=True)
    capacidad=models.CharField('Capacidad de Memoria', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.capacidad

class TipoDisco(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField('Tipo de Disco', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.tipo

class CapacidadDisco(models.Model):
    id=models.AutoField(primary_key=True)
    capacidad=models.CharField('Capacidad de Disco', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    def __str__(self):
        return self.capacidad

class TipoSO(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField('Tipo de Sistema Operativo', max_length=50,blank=False,null=False)
    version = models.CharField('Tipo de Sistema Operativo', max_length=50,blank=False,null=False)
    borrado = models.BooleanField('borrado',default=False)

    class Meta:
        verbose_name = 'TipoSO'
        verbose_name_plural = 'TipoSO'

    def __str__(self):
        return str(self.tipo) + ' ' + str(self.version)

    def save(self, *args, **kwargs):
        self.tipo = (self.tipo).upper()
        self.version = (self.tipo).upper()
        return super(TipoSO, self).save(*args, **kwargs)



##################################### Modelo de Tipo de Equipo ##########################################
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

##################################### Modelo de Estado ##########################################
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

##################################### Modelo de Marca ##########################################
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


##################################### Modelo de categoria de blog ##########################################
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('categoria activada/categoria desactivada', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return str(self.nombre)

##################################### Modelo de autor de blog ##########################################
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del autor', max_length = 100, null = False, blank = False)
    apellido = models.CharField('Apellido del autor', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Autor activo/Autor no activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return str(self.nombre) + ' ' + str(self.apellido)

##################################### Modelo Blog ##########################################
class Blog(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('titulo del blog', max_length = 100, null = False, blank = False)
    slug = models.CharField('slug del blog', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('descripcion del blog', max_length = 200, null = False, blank = False)
    contenido = RichTextField()
    url1 = models.URLField('Referencias para resolver un problema',max_length = 255, null = True, blank = True)
    url2 = models.URLField('Referencias para resolver un problema',max_length = 255, null = True, blank = True)
    url3 = models.URLField('Referencias para resolver un problema',max_length = 255, null = True, blank = True)
    imagen = models.URLField(max_length = 255, null = True, blank = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('blog activo/blog no activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now = True,auto_now_add = False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return str(self.titulo)



##################################### Modelo de Equipo ##########################################
class Equipo(models.Model):
    id = models.AutoField('Codigo de Servicio', primary_key = True, null = False, blank = False)
    tipoEquipo = models.ForeignKey(TipoEquipo, on_delete = models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete = models.PROTECT)
    modelo = models.CharField('Modelo del equipo', max_length = 100, null = False, blank = False)
    cliente = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    memoria = models.ForeignKey(TipoMemoria,on_delete = models.PROTECT,null = True, blank = True)
    capacidadMemoria = models.ForeignKey(CapacidadMemoria,on_delete = models.PROTECT,null = True, blank = True)
    disco = models.ForeignKey(TipoDisco,on_delete = models.PROTECT,null = True, blank = True)
    capacidadDisco = models.ForeignKey(CapacidadDisco,on_delete = models.PROTECT,null = True, blank = True)
    sistemaOperativo = models.ForeignKey(TipoSO,on_delete = models.PROTECT,null = True, blank = True)
    

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['cliente']
    
    def __str__(self):
        return str(self.marca) + ' - ' + str(self.modelo)

################################## Modelo de Estado de Repuesto ##################################
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

################################## Modelo de Tipo de Memoria ##################################
class Tipo_Memoria(models.Model):
    id = models.AutoField(primary_key = True)
    memoria = models.CharField('Tipo de memoria', max_length = 100, null = False, blank = False)
    capacidad = models.CharField('Capacidad de memoria', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Tipo_Memoria'
        verbose_name_plural = 'Tipos_de_Memoria'
    
    def __str__(self):
        return str(self.memoria) + ' - ' + str(self.capacidad)

    def save(self, *args, **kwargs):
        self.memoria = (self.memoria).upper()
        return super(Tipo_Memoria, self).save(*args, **kwargs)

################################## Modelo de Tipo de Discos ##################################
class Tipo_Disco(models.Model):
    id = models.AutoField(primary_key = True)
    disco = models.CharField('Tipo de disco', max_length = 100, null = False, blank = False)
    capacidad = models.CharField('Capacidad de disco', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Tipo_Disco'
        verbose_name_plural = 'Tipos_de_Disco'
    
    def __str__(self):
        return str(self.disco) + ' - ' + str(self.capacidad)

    def save(self, *args, **kwargs):
        self.disco = (self.disco).upper()
        return super(Tipo_Disco, self).save(*args, **kwargs)

################################## Modelo de Tipo de Sistema Operativo ##################################
class Tipo_Sistema_Operativo(models.Model):
    id = models.AutoField(primary_key = True)
    sistemaOperativo = models.CharField('Tipo de Sistema Operativo', max_length = 100, null = False, blank = False)
    version = models.CharField('Version del Sistema Operativo', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Tipo_Sistema_Operativo'
        verbose_name_plural = 'Tipos_Sistemas_Operativos'
    
    def __str__(self):
        return str(self.sistemaOperativo) + ' - ' + str(self.version)

    def save(self, *args, **kwargs):
        self.sistemaOperativo = (self.sistemaOperativo).upper()
        return super(Tipo_Sistema_Operativo, self).save(*args, **kwargs)

################################## Modelo de Accesorios ###########################################
class Accesorio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre Accesorio', max_length = 100, null = False, blank = False)
    
    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorio'
    
    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()
        return super(Accesorio, self).save(*args, **kwargs)


################################## Modelo de Servicio Tecnico ###########################################
class Servicio_Tecnico(models.Model):
    codServicio = models.AutoField('Codigo de Servicio', primary_key = True, null = False, blank = False)
    fechaIngreso = models.DateField('Fecha de Ingreso', null = False, blank = False)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)
    problema = models.CharField('Descripcion del problema', max_length = 120, null = False, blank = False)
    contraseña = models.CharField('Contraseña del equipo', max_length = 50, null = True, blank = True)
    accesorio = models.ForeignKey(Accesorio, on_delete = models.PROTECT)
    fechaEntrega = models.DateField('Fecha de Entrega', null = True, blank = True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null = True, blank=True, validators=[MinValueValidator(0.00)], default=0)
    trabajosRealizados = models.CharField('Trabajos realizados sobre el equipo', max_length = 120, null = True, blank = True)
    ubicacion = models.CharField('Ubicacion o Estante en el que se encuentra', max_length = 30, null = True, blank = True)
    equipo = models.ForeignKey(Equipo, on_delete = models.PROTECT)
    tecnico = models.ForeignKey(Tecnico, on_delete = models.PROTECT, null = True, blank = True)

    #repuesto = models.ForeignKey(Repuesto, on_delete = models.PROTECT)

    class Meta:
        verbose_name = 'Servicio_Tecnico'
        verbose_name_plural = 'Servicios_Tecnicos'
        ordering = ['codServicio']

    def __str__(self):
        return str(self.codServicio) + ' - ' + str(self.equipo) + ' - '

################################## Modelo de Repuesto ##################################
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