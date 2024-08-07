# Generated by Django 5.0.6 on 2024-07-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_note_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='Slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/preview', verbose_name='Превью (изображение)')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Дата создания (записи в БД)')),
                ('publication_sing', models.BooleanField(default=True, verbose_name='Признак публикации')),
                ('number_of_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
