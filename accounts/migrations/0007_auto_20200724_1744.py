# Generated by Django 3.0.1 on 2020-07-24 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200724_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_crated',
        ),
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 24, 17, 44, 31, 954563)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 24, 17, 44, 31, 923321)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 24, 17, 44, 31, 954563)),
        ),
    ]
