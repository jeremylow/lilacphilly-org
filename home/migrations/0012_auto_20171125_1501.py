# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 20:01
from __future__ import unicode_literals

import common.blocks
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170802_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('banner_image', wagtail.wagtailcore.blocks.StructBlock((('photo', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=False))))), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('photo_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')])), ('caption', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('caption_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('tl', 'Left'), ('tr', 'Right'), ('tc', 'Center')]))))), ('h1', common.blocks.HeaderH1(classname='full title')), ('subhead', common.blocks.Subhead(classname='full title')), ('block_quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock(classname='full', max_length=255, required=True)),))), ('call_to_action', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('cta_copy', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('button_title', wagtail.wagtailcore.blocks.CharBlock(max_length=255)), ('button_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('button_external_link', wagtail.wagtailcore.blocks.URLBlock(required=False))))), ('small_call_to_action', wagtail.wagtailcore.blocks.StructBlock((('button_copy', wagtail.wagtailcore.blocks.CharBlock(max_length=32)), ('button_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('button_external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('tl', 'Left'), ('tr', 'Right'), ('tc', 'Center')]))))), ('embed_code', wagtail.wagtailcore.blocks.StructBlock((('embed_code', wagtail.wagtailcore.blocks.TextBlock(required=True)),))))),
        ),
    ]
