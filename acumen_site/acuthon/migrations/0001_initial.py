# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('college', models.CharField(max_length=128)),
                ('year', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], default='I', max_length=3)),
                ('branch', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=256)),
                ('contact', models.CharField(max_length=15)),
                ('payment_id', models.CharField(max_length=256)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('project_link', models.CharField(max_length=1024)),
                ('theme', models.CharField(choices=[('NGO APPLICATIONS', 'NGO APPLICATIONS'), ('XR - AR/MR/VR', 'XR - AR/MR/VR'), ('SMART CITY', 'SMART CITY'), ('WOMEN SAFETY', 'WOMEN SAFETY'), ('EDUTAINMENT', 'EDUTAINMENT'), ('INTELLIGENTS APPLICATIONS', 'INTELLIGENTS APPLICATIONS')], max_length=64)),
            ],
        ),
    ]
