# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-28 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('senti', '0002_auto_20190628_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='password',
            new_name='Password',
        ),
    ]
