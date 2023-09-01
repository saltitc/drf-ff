from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "author", "tags")
    fields = ("title", "slug", "description", "content", "image", "created_at", "author", "tags")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    search_fields = ("title",)
    ordering = ("-title",)
