from django.db import models

from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey

from common.models import BaseModelWithUID


class BlogPage(BaseModelWithUID, Page):
    """Blog page model."""

    template = "blog/blog_page.html"

    intro = models.CharField(max_length=250, null=True)
    body = RichTextField(null=True)
    blog_images = models.ManyToManyField(
        "wagtailimages.Image",
        blank=True,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallery Images"),
    ]

    class GalleryImage(Orderable):
        page = ParentalKey(
            "BlogPage", on_delete=models.CASCADE, related_name="gallery_images"
        )
        image = models.ForeignKey(
            "wagtailimages.Image",
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name="+",
        )

        panels = [
            FieldPanel("image"),
        ]

    objects = Page.objects

    class Meta:
        verbose_name = "Blog Page"
        verbose_name_plural = "Blog Pages"
