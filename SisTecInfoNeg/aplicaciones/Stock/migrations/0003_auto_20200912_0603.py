# Generated by Django 3.0.8 on 2020-09-12 09:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0002_tipomovimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='LugarAlmacen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Almacen/Deposito')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion del Almacen/Deposito')),
            ],
            options={
                'verbose_name': 'Lugar de Alamcen',
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='TipoComprobante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Comprobante')),
            ],
            options={
                'verbose_name': 'Tipo de Comprobante',
                'verbose_name_plural': 'Comprobantes',
            },
        ),
        migrations.AddField(
            model_name='articulo',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precioCompra',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='articulo',
            name='precioVenta',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del moovimiento')),
                ('fechaMovimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Movimiento')),
                ('observaciones', models.CharField(max_length=200, verbose_name='Observaciones')),
                ('estado', models.BooleanField(default=True, verbose_name='activo/inactivo')),
                ('lugar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Stock.LugarAlmacen')),
                ('tipoComprobante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Stock.TipoComprobante')),
                ('tipoMovimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Stock.TipoMovimiento')),
            ],
            options={
                'verbose_name': 'Tipo de Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
        ),
    ]