# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-13 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wenjuan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question_list',
            name='t1',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='question_list',
            name='t1s',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='question_list',
            name='t3',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='question_list',
            name='t3s',
            field=models.CharField(max_length=64),
        ),
    ]
