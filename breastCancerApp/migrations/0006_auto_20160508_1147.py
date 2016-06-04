# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-08 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breastCancerApp', '0005_auto_20160508_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectitem',
            name='foreign_Key',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='breastCancerApp.Subject', verbose_name='外键'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectitem',
            name='subjectItemDescription',
            field=models.TextField(blank=True, default=1, verbose_name='描述'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjectitem',
            name='subjectItemDetailDescription',
            field=models.TextField(blank=True, default=1, verbose_name='详细描述'),
            preserve_default=False,
        ),
    ]