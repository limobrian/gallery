# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-19 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='pics/')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='firstapp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to='firstapp.Location'),
        ),
    ]
