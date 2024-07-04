from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='Slug', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='blog/preview', verbose_name='Превью (изображение)', **NULLABLE)
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания (записи в БД)')
    publication_sing = models.BooleanField(default=True, verbose_name='Признак публикации')
    number_of_views = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title} {self.body} {self.publication_sing} {self.number_of_views}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'