from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Класс для регистрации публикации в админке."""
    search_fields = ('title', 'is_published',)
    prepopulated_fields = {"slug": ("title",)}