# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 15:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lines', '0007_auto_20180117_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('desc', models.TextField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='lines.Line')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='', max_length=200)),
                ('desc', models.TextField()),
                ('due', models.DateTimeField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='lines.Line')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='lines.Line'),
        ),
    ]
