# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170310_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='coverletter',
        ),
    ]
