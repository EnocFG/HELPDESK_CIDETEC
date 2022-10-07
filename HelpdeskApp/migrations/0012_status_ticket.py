# Generated by Django 4.1.1 on 2022-10-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0011_prioridad'),
    ]

    operations = [
        migrations.CreateModel(
            name='status_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estatus', models.CharField(choices=[('1', 'Creado'), ('2', 'Atendido'), ('3', 'Asignado'), ('4', 'Proceso'), ('5', 'Espera'), ('6', 'Resuelto'), ('7', 'Validado'), ('8', 'Cancelado'), ('9', 'Reasignado')], default='1', max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_culminacion', models.DateTimeField()),
            ],
        ),
    ]
