from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='человекопонятный URL', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    preview = models.ImageField(upload_to='preview/photo', verbose_name='Превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication = models.BooleanField(verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
