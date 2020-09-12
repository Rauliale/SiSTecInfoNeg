from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Articulo', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        permissions = (("es_categoria", "es categoria"),("es_pre_categoria", "es pre categoria"))

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(Categoria, self).save(*args, **kwargs)

#Sirve para agrupar tipos de articulos
class Grupo(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Grupo', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        permissions = (("es_grupo", "es grupo"),("es_pre_grupo", "es pre grupo"))

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(Grupo, self).save(*args, **kwargs)

class Unidad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la unidad', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        permissions = (("es_unidad", "es unidad"),("es_pre_unidad", "es pre unidad"))

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(Unidad, self).save(*args, **kwargs)

class TipoMovimiento(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del moovimiento', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'TiposMovimientos'

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(TipoMovimiento, self).save(*args, **kwargs)

class TipoComprobante(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Comprobante', max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Tipo de Comprobante'
        verbose_name_plural = 'Comprobantes'

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(TipoComprobante, self).save(*args, **kwargs)

class TipoImpuesto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Impuesto', max_length = 100, null = False, blank = False)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    
    class Meta:
        verbose_name = 'Tipo de Impuesto'
        verbose_name_plural = 'Impuestos'

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(TipoImpuesto, self).save(*args, **kwargs)

class Ganancias(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Porcentage de Ganancia', max_length = 100, null = False, blank = False)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    
    class Meta:
        verbose_name = 'Ganancia'
        verbose_name_plural = 'Ganancias'

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(Ganancias, self).save(*args, **kwargs)


class LugarAlmacen(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre del Almacen/Deposito', max_length = 100, null = False, blank = False)
    direccion = models.CharField('Direccion del Almacen/Deposito', max_length = 200, null = False, blank = False)

    class Meta:
        verbose_name = 'LugardeAlamcen'
        verbose_name_plural = 'Almacenes'

    def __str__(self):
            return str(self.nombre)
           

    def save(self, *args, **kwargs):
        self.nombre = (self.nombre).upper()        
        return super(LugarAlmacen, self).save(*args, **kwargs)

class Articulo(models.Model):
    id =  models.AutoField(primary_key = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING,  null = True, blank = True)
    nombreArticulo = models.CharField('Nombre del Articulo', max_length = 100, null = False, blank = False)
    grupo = models.ForeignKey(Grupo, on_delete = models.DO_NOTHING,  null = True, blank = True)
    stockMinimo = models.DecimalField(max_digits=10, decimal_places=0,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    unidadMedida = models.ForeignKey(Unidad, on_delete = models.DO_NOTHING,  null = True, blank = True)
    precioCompra = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    precioVenta = models.DecimalField(max_digits=10, decimal_places=2,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    cantidad = models.DecimalField(max_digits=10, decimal_places=0,null = True, blank=True, validators=[MinValueValidator(0)], default=0) 
    estado = models.BooleanField('Articulo activo/inactivo', default = False)
    impuesto = models.ForeignKey(TipoImpuesto, on_delete = models.DO_NOTHING,  null = True, blank = True)
    ganancia = models.ForeignKey(Ganancias, on_delete = models.DO_NOTHING,  null = True, blank = True)
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        permissions = (("es_articulo", "es articulo"),("es_pre_articulo", "es pre articulo"))

    def __str__(self):
            return str(self.nombreArticulo)

    def save(self, *args, **kwargs):
        self.nombreArticulo = (self.nombreArticulo).upper()      
        return super(Articulo, self).save(*args, **kwargs)

class Movimiento(models.Model):
    id = models.AutoField(primary_key = True)
    tipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete = models.DO_NOTHING,  null = True, blank = True)
    tipoComprobante = models.ForeignKey(TipoComprobante, on_delete = models.DO_NOTHING,  null = True, blank = True)
    numeroComprobante = models.CharField('Numero de comprobante', max_length = 100, null = False, blank = False)
    lugar = models.ForeignKey(LugarAlmacen, on_delete = models.DO_NOTHING,  null = True, blank = True)
    fechaMovimiento = models.DateField('Fecha de Movimiento', null = True, blank = True)
    observaciones = models.CharField('Observaciones', max_length = 200, null = True, blank = True)
    estado = models.BooleanField('activo/inactivo', default = True)
    articulo = models.ForeignKey(Articulo, on_delete = models.DO_NOTHING,  null = True, blank = True)
    total = models.CharField('Total', max_length = 200, null = True, blank = True)

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'

    def __str__(self):
            return str(self.id) + ' - '+ str(self.tipoMovimiento)+' - '+ str(self.fechaMovimiento)
           

    def save(self, *args, **kwargs):
        return super(Movimiento, self).save(*args, **kwargs)


