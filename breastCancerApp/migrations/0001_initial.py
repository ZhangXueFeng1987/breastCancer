# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BreatCancerInformationItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectTypeItemName', models.CharField(max_length=30, verbose_name='子标题名称')),
            ],
        ),
        migrations.CreateModel(
            name='BreatCancerSubject',
            fields=[
                ('subjectPrimaryKey', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='主键(需与代码一致)')),
                ('subjectName', models.CharField(max_length=30, verbose_name='主题名称')),
                ('subjectDescription', models.TextField(verbose_name='描述')),
                ('subjectDisplaySequence', models.IntegerField(verbose_name='排序权重(数字)')),
            ],
            options={
                'verbose_name_plural': '标题',
            },
        ),
    ]
