# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-12-31 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='mailin/images')),
                ('colocacion', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('espacios', models.IntegerField()),
                ('template', models.CharField(max_length=140)),
                ('img_espacios', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='imagen',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='mailin.Template'),
        ),
    ]