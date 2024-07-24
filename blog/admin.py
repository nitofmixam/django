from django.contrib import admin
from blog.models import BlogArticle


@admin.register(BlogArticle)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "created_at", "is_published", "views_count")
    list_filter = ("is_published", )
    search_fields = ("title", "body")