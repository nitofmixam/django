from django.contrib import admin
from blog.models import Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "image_preview", "is_public", "count_view")
    list_filter = ("id", "title")
    search_fields = ("id", "title", "body")