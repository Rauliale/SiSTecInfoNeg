# Generated by Django 3.0.8 on 2020-08-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0007_auto_20200817_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Otro', 'Otro'), ('Claro', 'Claro'), ('Movistar', 'Movistar'), ('Personal', 'Personal'), ('Tuenti', 'Tuenti')], max_length=50, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='tipo_telefono',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Movil', 'Movil'), ('Fijo', 'Fijo')], max_length=50, null=True, verbose_name='Tipo'),
        ),
    ]