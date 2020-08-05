# Generated by Django 3.0.1 on 2020-08-03 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200803_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 23, 31, 6, 639387)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 23, 31, 6, 655008)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_crated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 23, 31, 6, 655008)),
        ),
    ]