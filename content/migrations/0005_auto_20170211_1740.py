# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20170211_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='/static/uploaded_pics/no-img.jpg', upload_to='/static/uploaded_pics/'),
        ),
    ]
