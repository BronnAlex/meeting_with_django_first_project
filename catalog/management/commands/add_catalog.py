from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):

        # Удаляем существующие записи из БД чтобы не было конфликтов
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Добавление данных в БД из фикстур
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Данные успешно загружены из фикстур"))

        # Добавление тестовых данных
        category_books, _ = Category.objects.get_or_create(
            name_category="Книги", description_category="Читаем с умом"
        )
        category_pens, _ = Category.objects.get_or_create(
            name_category="Ручки", description_category="Пишем красиво"
        )

        our_product = [
            {
                "name_product": "Мартин Иден",
                "description_product": "Великолепная книга",
                "category_product": category_books,
                "unit_price_product": 156,
                "created_at": "1850-01-02",
            },
            {
                "name_product": "Приключения",
                "description_product": "Великолепная книга",
                "category_product": category_books,
                "unit_price_product": 300,
                "created_at": "1850-01-02",
            },
            {
                "name_product": "Белый Клык",
                "description_product": "Великолепная книга",
                "category_product": category_books,
                "unit_price_product": 800,
                "created_at": "1850-01-02",
            },
            {
                "name_product": "Гелевая ручка",
                "description_product": "Черная паста",
                "category_product": category_pens,
                "unit_price_product": 30,
                "created_at": "1850-01-02",
            },
            {
                "name_product": "Шариковая ручка",
                "description_product": "Синяя паста",
                "category_product": category_pens,
                "unit_price_product": 25,
                "created_at": "1850-01-02",
            },
        ]

        for product_data in our_product:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Продукт успешно добавлен: {product.name_product}, {product.unit_price_product} рублей"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Такой продукт уже существует: {product.name_product}, {product.unit_price_product} рублей"
                    )
                )
