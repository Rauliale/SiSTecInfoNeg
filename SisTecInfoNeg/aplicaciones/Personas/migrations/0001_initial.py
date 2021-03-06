# Generated by Django 3.0.8 on 2020-10-06 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id_domicilio', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('nro', models.CharField(max_length=50, verbose_name='Numero')),
                ('mz', models.CharField(blank=True, max_length=50, null=True, verbose_name='Manzana')),
                ('departamento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento')),
                ('piso', models.CharField(blank=True, max_length=50, null=True, verbose_name='Piso')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la especialidad')),
                ('descripcion', models.TextField(verbose_name='Descripcion de la especialidad')),
                ('estadoEsp', models.BooleanField(default=True, verbose_name='activo/inactivo')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_provincia', models.AutoField(primary_key=True, serialize=False)),
                ('provincia', models.CharField(max_length=50, verbose_name='Provincia')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del rol')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion del rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Telefono',
            fields=[
                ('id_tipo_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, choices=[('Fijo', 'Fijo'), ('Movil', 'Movil')], max_length=50, null=True, verbose_name='Tipo')),
                ('empresa', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Tuenti', 'Tuenti'), ('Movistar', 'Movistar'), ('Claro', 'Claro'), ('Otro', 'Otro')], max_length=50, null=True, verbose_name='Empresa')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id_telefono', models.AutoField(primary_key=True, serialize=False)),
                ('prefijo', models.IntegerField(blank=True, null=True, verbose_name='Prefijo')),
                ('numero', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('whatsapp', models.BooleanField(default=True, verbose_name='Whatsapp')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('tipo_telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.Tipo_Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('turno', models.CharField(blank=True, max_length=100, null=True, verbose_name='Turno de trabajo del tecnico')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.Domicilio')),
                ('especialidades', models.ManyToManyField(blank=True, to='Personas.Especialidad')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.Rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.Telefono')),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'permissions': (('es_Tecnico', 'es Tecnico'), ('es_pre_Tecnico', 'es pre Tecnico')),
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id_localidad', models.AutoField(primary_key=True, serialize=False)),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('borrado', models.BooleanField(default=False, verbose_name='borrado')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.Provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('turno', models.CharField(max_length=100, verbose_name='Turno de trabajo del Empleado')),
                ('puesto', models.CharField(max_length=100, verbose_name='Puesto de trabajo del Empleado')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.Domicilio')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.Rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.Telefono')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'permissions': (('es_Empleado', 'es Empleado'), ('es_pre_Empleado', 'es pre Empleado')),
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('dni', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellido del usuario')),
                ('fechaNac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo de la persona')),
                ('correoElectronico', models.EmailField(max_length=254, verbose_name='Correo electronico del usuario')),
                ('estado', models.BooleanField(default=False, verbose_name='Usuario activo/inactivo')),
                ('nombreEmpresa', models.TextField(blank=True, null=True, verbose_name='Empresa del cliente')),
                ('domicilio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Personas.Domicilio')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Personas.Rol')),
                ('telefono', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Personas.Telefono')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'permissions': (('es_cliente', 'es cliente'), ('es_pre_cliente', 'es pre cliente')),
            },
        ),
    ]
