# Generated by Django 3.0.1 on 2020-07-23 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 23, 16, 12, 752779)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 23, 16, 12, 752779)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 23, 16, 12, 752779)),
        ),
    ]
