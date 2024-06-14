from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('category.json', encoding='windows-1251') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('product.json', encoding='windows-1251') as file:
            return json.load(file)

    def handle(self, *args, **options):

        # Удаляем все категории
        Category.objects.all().delete()
        # Удаляем все продукты
        Product.objects.all().delete()
        # Создаём списки для хранения объектов
        category_for_create = []
        product_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name=category["fields"]["name"],
                         description=category["fields"]["description"])
            )
        # print(category_for_create)
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], name=product["fields"]["name"],
                        description=product["fields"]["description"],
                        image=product["fields"]["image"],
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)