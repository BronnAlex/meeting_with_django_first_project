from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


class ProductService:
    """Сервисный класс для работы с продуктами, где метод будет возвращает
    список всех продуктов в указанной категории."""

    @staticmethod
    def get_products_in_category():
        """Статический метод для возврата списка продуктов из конкретной категории"""
        # # по переданному id получаем связанные с продуктами категории
        # category = Category.objects.filter(name_category=name_category)
        # if not category.exists():
        #     return None
        #
        # product_list = [product.name_category for product in category]
        # return product_list
        """
            Возвращает словарь, где ключ - категория, а значение - QuerySet продуктов этой категории.
            """
        products_by_category = {}
        categories = Category.objects.all()  # Получаем все категории
        for category in categories:
            # Используем related_name 'products' для получения продуктов категории
            products = category.products.all().order_by(
                "name_product"
            )  # QuerySet продуктов
            products_by_category[category] = products
        return products_by_category

    # Пример использования:
    # products_per_category = get_products_in_category()
    # for category, products in products_per_category.items():
    #     print(f"Категория: {category.name}")
    #     if products:
    #         for product in products:
    #             print(f"  - {product.name}")
    #     else:
    #         print("  - Нет продуктов в этой категории")


def products_from_cache():
    """Функция проверки, есть ли объекты в кэше"""
    if (
        not CACHE_ENABLED
    ):  # Если кэширование не включено в проект, то возвр объекты из БД
        return Product.objects.all()

    key = "product_list"
    products = cache.get(key)
    # если продукты есть в кэше, получаем из кэша
    if products is not None:
        return products

    # если продуктов нет в кэше, то добавляем их в кэш
    products = Product.objects.all()
    cache.set(key, products)
    return products
