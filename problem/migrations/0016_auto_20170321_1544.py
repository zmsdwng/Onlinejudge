# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-21 07:44
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0015_problemdiscussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemdiscussion',
            name='message',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
