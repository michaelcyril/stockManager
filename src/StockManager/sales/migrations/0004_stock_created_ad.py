# Generated by Django 3.2.15 on 2022-08-10 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20220809_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='created_ad',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 8, 10, 19, 48, 42, 135386)),
        ),
    ]