# Generated by Django 3.0.8 on 2020-09-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0007_movimiento_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='total',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Total'),
        ),
    ]
