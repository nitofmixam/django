from django.db import models

from catalog.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='загаловок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='содержимое')
    image = models.ImageField(upload_to='products/photo/', **NULLABLE,
                              verbose_name='изображение')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name='дата создания')

    is_published = models.BooleanField(default=True,
                                       verbose_name='опубликован')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'