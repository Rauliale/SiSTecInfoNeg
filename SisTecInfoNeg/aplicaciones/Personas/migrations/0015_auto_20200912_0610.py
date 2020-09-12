# Generated by Django 3.0.8 on 2020-09-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0014_auto_20200912_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Claro', 'Claro'), ('Movistar', 'Movistar'), ('Personal', 'Personal'), ('Tuenti', 'Tuenti'), ('Otro', 'Otro')], max_length=50, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='tipo_telefono',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Fijo', 'Fijo'), ('Movil', 'Movil')], max_length=50, null=True, verbose_name='Tipo'),
        ),
    ]