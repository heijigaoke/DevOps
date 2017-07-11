# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anweb', '0010_auto_20170508_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='oper_group',
        ),
        migrations.AddField(
            model_name='history',
            name='oper_hostlist',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AddField(
            model_name='history',
            name='oper_result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='anweb.State'),
        ),
        migrations.AlterField(
            model_name='history',
            name='oper_info',
            field=models.CharField(default='NULL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='history',
            name='oper_time',
            field=models.DateField(auto_now=True),
        ),
    ]
