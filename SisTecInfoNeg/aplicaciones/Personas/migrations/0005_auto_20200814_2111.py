# Generated by Django 3.0.8 on 2020-08-15 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0004_auto_20200814_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Tuenti', 'Tuenti'), ('Movistar', 'Movistar'), ('Personal', 'Personal'), ('Otro', 'Otro'), ('Claro', 'Claro')], max_length=50, null=True, verbose_name='Empresa'),
        ),
    ]
