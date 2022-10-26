# Generated by Django 4.1.1 on 2022-10-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0014_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='historial_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_modificacion', models.DateTimeField(verbose_name='Fecha modificacion')),
                ('especialista_anterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.especialista')),
                ('ht_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.ticket')),
                ('ht_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.usuario')),
                ('status_anterior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HelpdeskApp.status_ticket')),
            ],
        ),
    ]