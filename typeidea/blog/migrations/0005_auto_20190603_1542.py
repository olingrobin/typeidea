# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-03 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tag',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
