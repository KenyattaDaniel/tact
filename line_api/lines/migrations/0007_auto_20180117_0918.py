# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0006_auto_20180109_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line', to='lines.Line'),
        ),
    ]
