# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('gcm_id', models.TextField()),
            ],
        ),
    ]
