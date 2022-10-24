# Generated by Django 4.1.1 on 2022-10-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status_E',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estatus', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO', max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha incial')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha final')),
            ],
        ),
    ]
