# Generated by Django 5.0.6 on 2024-07-24 15:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'category'], 'permissions': [('can_edit_description', 'Can edit description'), ('can_edit_category', 'Can edit category'), ('can_change_is_published', 'Can change sign of publication')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ['number'], 'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='version',
            name='version_name',
        ),
        migrations.RemoveField(
            model_name='version',
            name='version_number',
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опупликован'),
        ),
        migrations.AddField(
            model_name='product',
            name='preview',
            field=models.ImageField(blank=True, help_text='Добавьте изображение товара', null=True, upload_to='products/photo', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='version',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='version',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите наименование категории', max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Введите категорию товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание товара', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Введите наименование товара', max_length=100, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активная'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт'),
        ),
    ]
