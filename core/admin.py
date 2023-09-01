from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "author", "tags")
    fields = ("title", "slug", "description", "content", "image", "created_at", "author", "tags")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    search_fields = ("title",)
    ordering = ("-title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "username", "text", "created_date")
    fields = ("post", "username", "text", "created_date")
    readonly_fields = ("created_date",)
    search_fields = ("username",)
    ordering = ("-created_date",)
