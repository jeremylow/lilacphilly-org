# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_toplevelpage_page_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FundraisingSnippet',
            new_name='EmbedCodeSnippet',
        ),
    ]
