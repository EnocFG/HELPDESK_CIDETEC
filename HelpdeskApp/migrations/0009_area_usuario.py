# Generated by Django 4.1.1 on 2022-10-07 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0008_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='area_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_created=True)),
                ('fecha_culminacion', models.DateTimeField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.area')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.proyecto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.usuario')),
            ],
        ),
    ]