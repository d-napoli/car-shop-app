# Generated by Django 3.2.6 on 2021-08-21 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionaria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='carro',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
