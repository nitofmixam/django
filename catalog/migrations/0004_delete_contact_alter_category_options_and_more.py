# Generated by Django 5.0.6 on 2024-07-26 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_contact_alter_category_options_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'permissions': [('can_canceled_public', 'может отменять публикацию продукта'), ('can_edit_category ', 'может менять описание любого продукта'), ('can_edit_desk', 'может менять категорию любого продукта')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='product',
            name='preview',
        ),
        migrations.RemoveField(
            model_name='version',
            name='name',
        ),
        migrations.RemoveField(
            model_name='version',
            name='number',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/photo', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='version',
            name='version_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название версии'),
        ),
        migrations.AddField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите наименование товара', max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Влааделец'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт'),
        ),
    ]
