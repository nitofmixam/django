# Generated by Django 5.0.6 on 2024-08-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_options_remove_blog_blog_img_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='count_view',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_preview',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_img',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью статьи'),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Статья'),
        ),
        migrations.AddField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
    ]
