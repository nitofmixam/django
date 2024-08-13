# Generated by Django 4.2.1 on 2024-08-13 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Изображение (превью)')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='цена')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Дата последнего изменения')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукт',
                'ordering': ('name',),
                'permissions': [('set_published', 'Can publish product'), ('change_description', 'Can change description'), ('change_category', 'Can change category')],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер версии')),
                ('version_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]
