# Generated by Django 2.0.7 on 2018-08-20 13:58

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
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 20, 11, 58, 25, 167962), verbose_name='Tempo da proposta'),
        ),
    ]