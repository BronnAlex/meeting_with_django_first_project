from django.contrib import admin

from .models import BlogEntry


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "created_at",
    )
    list_filter = ("title", "created_at")
    search_fields = (
        "title",
        "content",
    )
