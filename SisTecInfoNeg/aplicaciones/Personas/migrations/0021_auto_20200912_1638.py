# Generated by Django 3.0.8 on 2020-09-12 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0020_auto_20200912_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_telefono',
            name='empresa',
            field=models.CharField(blank=True, choices=[('Tuenti', 'Tuenti'), ('Otro', 'Otro'), ('Personal', 'Personal'), ('Claro', 'Claro'), ('Movistar', 'Movistar')], max_length=50, null=True, verbose_name='Empresa'),
        ),
    ]