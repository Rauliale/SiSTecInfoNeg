# Generated by Django 3.0.8 on 2020-08-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0006_auto_20200815_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Movistar', 'Movistar'), ('Tuenti', 'Tuenti'), ('Otro', 'Otro'), ('Personal', 'Personal'), ('Claro', 'Claro')], max_length=50, null=True, verbose_name='Empresa'),
        ),
    ]
