# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-13 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1s', models.CharField(max_length=32)),
                ('t1', models.CharField(max_length=32)),
                ('t3s', models.CharField(max_length=32)),
                ('t3', models.CharField(max_length=32)),
            ],
        ),
    ]
