# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(),
        ),
    ]
