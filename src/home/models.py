from django.db import models
from django.template.defaultfilters import truncatechars

from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"  # default template. Can be overridden in the admin

    banner_title = models.CharField(max_length=100, null=True)
    banner_subtitle = RichTextField(null=True, blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
    ]

    @property
    def short_title(self):
        return truncatechars(self.title, 40)

    @property
    def short_banner_title(self):
        return truncatechars(self.banner_title, 40)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
