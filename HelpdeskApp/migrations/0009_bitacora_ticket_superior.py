# Generated by Django 4.1 on 2022-11-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpdeskApp', '0008_respaldo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitacora',
            name='ticket_superior',
            field=models.BigIntegerField(null=True),
        ),
    ]
