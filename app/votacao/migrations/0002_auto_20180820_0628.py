# Generated by Django 2.1 on 2018-08-20 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='tempo_final',
            field=models.TimeField(default=datetime.datetime(2018, 8, 20, 7, 28, 25, 85255), verbose_name='Tempo da proposta'),
        ),
    ]
