# Generated by Django 3.2.2 on 2022-09-01 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220901_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomuser',
            name='joined',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
