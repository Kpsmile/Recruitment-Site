# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170310_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Noticeperiod',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='currentsalary',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='expectedsalary',
            field=models.IntegerField(null=True),
        ),
    ]