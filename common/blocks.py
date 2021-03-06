# -*- coding: utf-8 -*-

"""Common structblocks for use in editor."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BlockQuote(blocks.StructBlock):
    """Create a block quote StructBlock element."""

    quote = blocks.TextBlock(required=True, max_length=255, classname="full")

    class Meta:
        """Implement class specific attrs here."""

        icon = "openquote"
        template = "common/_block_quote.html"


class CaptionImageBlock(blocks.StructBlock):
    """Create an image with caption and optional alignment."""

    photo = ImageChooserBlock()
    photo_alignment = blocks.ChoiceBlock(
        choices=(("left", "Left"), ("right", "Right"), ("center", "Center"))
    )
    caption = blocks.CharBlock(max_length=255)
    caption_alignment = blocks.ChoiceBlock(
        choices=(("tl", "Left"), ("tr", "Right"), ("tc", "Center"))
    )

    class Meta:
        """Class specific attrbutes."""

        icon = "image"
        template = "common/_captioned_image_block.html"


class HeaderH1(blocks.CharBlock):
    """Create an H1 header."""

    class Meta:
        """Class specific attributes."""

        icon = "title"
        template = "common/_h1.html"


class Subhead(blocks.CharBlock):
    """Create a subhead for use within page."""

    class Meta:
        """Class specific attributes."""

        icon = "title"
        template = "common/_subhead.html"


class CallToAction(blocks.StructBlock):
    """Create a call to action for use within page."""

    title = blocks.CharBlock(max_length=255)
    cta_copy = blocks.CharBlock(max_length=255)
    button_title = blocks.CharBlock(max_length=255)
    button_link = blocks.PageChooserBlock(required=False)
    button_external_link = blocks.URLBlock(required=False)

    class Meta:
        """Class specific attributes."""

        icon = "title"
        template = "common/_cta.html"


class BannerImage(blocks.StructBlock):
    """Create a full-width banner image.

    Optionally, you can specify a link and clicking on the image will
    go to that page or URL.

    """

    photo = ImageChooserBlock(required=True)
    internal_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)
    alt_text = blocks.CharBlock(max_length=255, required=False)

    class Meta:
        """Class specific attributes."""

        icon = "image"
        template = "common/_banner_image_link.html"


class CTAButton(blocks.StructBlock):
    """Small button for a call to action."""

    button_copy = blocks.CharBlock(max_length=32)
    button_link = blocks.PageChooserBlock(required=False)
    button_external_link = blocks.URLBlock(required=False)
    alignment = blocks.ChoiceBlock(
        choices=(("tl", "Left"), ("tr", "Right"), ("tc", "Center"))
    )

    class Meta:
        """Specific attributes."""

        icon = "title"
        template = "common/_cta_button.html"


class EmbedCode(blocks.StructBlock):
    """Block for embed codes."""

    embed_code = blocks.TextBlock(required=True)

    class Meta:
        """Specific attrs."""

        icon = "code"
        template = "common/_embed_code.html"
