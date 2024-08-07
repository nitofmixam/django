# Generated by Django 5.0.6 on 2024-07-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogarticle_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='человекопонятный URL')),
                ('text', models.TextField(verbose_name='Текст')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='preview/photo', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publication', models.BooleanField(verbose_name='Опубликовано')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
        migrations.DeleteModel(
            name='BlogArticle',
        ),
    ]
