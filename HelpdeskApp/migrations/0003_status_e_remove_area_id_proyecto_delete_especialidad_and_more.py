# Generated by Django 4.1.1 on 2022-10-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0002_alter_area_id_proyecto'),
    ]

    operations = [
        migrations.CreateModel(
            name='status_e',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estatus', models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_culminacion', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='area',
            name='id_proyecto',
        ),
        migrations.DeleteModel(
            name='especialidad',
        ),
        migrations.DeleteModel(
            name='prioridad',
        ),
        migrations.DeleteModel(
            name='rol',
        ),
        migrations.DeleteModel(
            name='status',
        ),
        migrations.DeleteModel(
            name='area',
        ),
        migrations.DeleteModel(
            name='proyecto',
        ),
    ]
