# Generated by Django 3.0.8 on 2020-09-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0018_auto_20200912_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Movistar', 'Movistar'), ('Otro', 'Otro'), ('Claro', 'Claro'), ('Personal', 'Personal'), ('Tuenti', 'Tuenti')], max_length=50, null=True, verbose_name='Empresa'),
        ),
    ]