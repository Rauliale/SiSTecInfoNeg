# Generated by Django 3.0.8 on 2020-09-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0009_auto_20200908_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Claro', 'Claro'), ('Otro', 'Otro'), ('Movistar', 'Movistar'), ('Tuenti', 'Tuenti'), ('Personal', 'Personal')], max_length=50, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='tipo_telefono',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Fijo', 'Fijo'), ('Movil', 'Movil')], max_length=50, null=True, verbose_name='Tipo'),
        ),
    ]