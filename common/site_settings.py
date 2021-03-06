# -*- coding: utf-8 -*-
from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SocialMediaSettings(BaseSetting):
    """Set social media urls for site.

    These profiles are exported to JSON+LD for structured data.
    """

    facebook = models.URLField(blank=True, help_text="Your Facebook page URL")
    twitter = models.URLField(blank=True, help_text="Your twitter profile URL")
    twitter_screen_name = models.CharField(
        blank=True, max_length=16, help_text='Your twitter screenname (with the "@"'
    )
    instagram = models.URLField(blank=True, help_text="Your Instagram profile URL")
    youtube = models.URLField(
        blank=True, help_text="Your YouTube channel or user account URL"
    )


@register_setting
class SEOSettings(BaseSetting):
    """Set site name and description for use with structured data."""

    organization_short_name = models.CharField(
        max_length=255, help_text="The actual name of your local (ie. Philly DSA"
    )
    organization_full_name = models.CharField(
        max_length=500,
        help_text="The actual name of your local (ie. Philadelphia Local of the Democratic [etc])",
    )
    address_street = models.CharField(
        max_length=255, help_text="Street address for local (if any)", blank=True
    )
    address_city = models.CharField(max_length=255, blank=True)
    address_state = models.CharField(max_length=255, blank=True)
    address_zip_code = models.CharField(max_length=5, blank=True)

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="The URL of the logo of your local. Ideally, should be 1200x1200",
    )
    logo_wide = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Wide-format logo URL. Should be less than 60px high and 600px wide.",
    )
    description = models.CharField(
        max_length=500,
        help_text="A short description of your local. City, what you are trying to achieve, etc.",
        blank=True,
    )
    keywords = models.CharField(
        max_length=1500,
        help_text="Comma separated list of keywords describing your website.",
        blank=True,
    )
    google_site_verification_key = models.CharField(
        max_length=255,
        help_text="Verification key for Google Webmaster Tools.",
        blank=True,
    )
    google_analytics_key = models.CharField(
        max_length=255,
        help_text="Google Analytics Key. Should be something like UA-101255774-1.",
        blank=True,
    )

    panels = [
        MultiFieldPanel(
            heading="Chapter Information",
            children=[
                FieldPanel("organization_short_name"),
                FieldPanel("organization_full_name"),
                FieldPanel("description"),
            ],
        ),
        MultiFieldPanel(
            heading="Address Information",
            children=[
                FieldPanel("address_street"),
                FieldPanel("address_city"),
                FieldPanel("address_state"),
                FieldPanel("address_zip_code"),
            ],
        ),
        ImageChooserPanel("logo"),
        ImageChooserPanel("logo_wide"),
        MultiFieldPanel(
            heading="Google Keys & Data",
            children=[
                FieldPanel("keywords"),
                FieldPanel("google_site_verification_key"),
                FieldPanel("google_analytics_key"),
            ],
        ),
    ]
