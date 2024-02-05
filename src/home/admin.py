from django.contrib import admin

from .models import HomePage


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    """Home page admin."""

    list_display = ["short_title", "short_banner_title"]
    search_fields = ["title"]
