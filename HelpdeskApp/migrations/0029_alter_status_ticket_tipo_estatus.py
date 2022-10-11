# Generated by Django 4.1.1 on 2022-10-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0028_alter_status_e_tipo_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status_ticket',
            name='tipo_estatus',
            field=models.CharField(choices=[('Creado', 'Creado'), ('Atendido', 'Atendido'), ('Asignado', 'Asignado'), ('Proceso', 'Proceso'), ('Espera', 'Espera'), ('Resuelto', 'Resuelto'), ('Validado', 'Validado'), ('Cancelado', 'Cancelado'), ('Reasignado', 'Reasignado')], default='Creado', max_length=10),
        ),
    ]