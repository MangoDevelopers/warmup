# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gcm_id',
            field=models.CharField(max_length=320),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=320),
        ),
    ]