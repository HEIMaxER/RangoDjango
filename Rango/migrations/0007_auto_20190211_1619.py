# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 16:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Rango', '0006_auto_20190211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='first_visit',
            field=models.DateField(default=datetime.datetime(2019, 2, 11, 16, 19, 36, 988555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateField(default=datetime.datetime(2019, 2, 11, 16, 19, 36, 988531, tzinfo=utc)),
        ),
    ]
