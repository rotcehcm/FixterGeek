# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-13 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20160512_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
