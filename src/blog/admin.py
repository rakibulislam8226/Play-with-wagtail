from django.contrib import admin

from .models import BlogPage


@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    """Blog page admin."""

    list_display = ["short_title", "short_intro"]
    search_fields = ["title", "intro"]
    date_hierarchy = "created_at"
