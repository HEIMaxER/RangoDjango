# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-11 16:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Rango', '0005_auto_20190211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='first_visit',
            field=models.DateField(default=datetime.datetime(2019, 2, 11, 16, 4, 6, 589792, tzinfo=utc)),
        ),
    ]