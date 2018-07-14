# Generated by Django 2.0.7 on 2018-07-14 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20180714_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='server_time_to',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 14, 16, 40, 42, 990098)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(2, 'Ready'), (4, 'Delivered'), (1, 'Cooking'), (3, 'On the way')]),
        ),
    ]