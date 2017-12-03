# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 21:55
from __future__ import unicode_literals

import common.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20170506_2113'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='fundraising_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.EmbedCodeSnippet'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('photo_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')])), ('caption', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('caption_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('tl', 'Left'), ('tr', 'Right'), ('tc', 'Center')]))))), ('h1', common.blocks.HeaderH1(classname='full title')), ('subhead', common.blocks.Subhead(classname='full title')), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock(classname='full', max_length=255, required=True)),))), ('dues_cta', common.blocks.CallToAction()))),
        ),
    ]
