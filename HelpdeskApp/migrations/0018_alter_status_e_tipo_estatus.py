# Generated by Django 4.1.1 on 2022-10-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0017_alter_especialidad_tipo_especialidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status_e',
            name='tipo_estatus',
            field=models.CharField(max_length=10),
        ),
    ]