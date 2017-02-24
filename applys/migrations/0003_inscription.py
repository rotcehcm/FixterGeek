# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-24 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applys', '0002_auto_20161231_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
                ('tel', models.CharField(max_length=140)),
                ('path', models.CharField(max_length=140)),
                ('beca', models.BooleanField(default=False)),
                ('why', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscripciones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]