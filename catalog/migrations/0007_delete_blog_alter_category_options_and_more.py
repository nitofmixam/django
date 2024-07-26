# Generated by Django 5.0.6 on 2024-07-26 18:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_blog_alter_product_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('delete_public_product', 'Can disable product'), ('change_product_description', 'Can change product description'), ('change_product_category', 'Can change product category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('product',), 'verbose_name': 'Версия продукта', 'verbose_name_plural': 'Версии продуктов'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='version',
            name='version_num',
        ),
        migrations.AddField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(blank=True, help_text='Загрузите фото товара', null=True, upload_to='products/photo', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
        migrations.AddField(
            model_name='version',
            name='version_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Введите строку названия категории', max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание товара', null=True, verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Введите строку названия товара', max_length=100, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, help_text='Введите строку стоимости товара', null=True, verbose_name='Стоимость товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(help_text='Активно?', verbose_name='Признак текущей версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_name',
            field=models.CharField(blank=True, help_text='Введите название версии', max_length=100, null=True, verbose_name='Название версии'),
        ),
    ]