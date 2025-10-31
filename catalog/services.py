from catalog.models import Product, Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache


class ProductService:
    """Сервисный класс для работы с продуктами, где метод будет возвращает
     список всех продуктов в указанной категории."""

    @staticmethod
    def service_category_product(name_category):
        """Статический метод для возврата списка продуктов из конкретной категории """
        # по переданному id получаем связанные с продуктами категории
        category = Category.objects.filter(name_category=name_category)
        if not category.exists():
            return None

        product_list = [product.name_category for product in category]
        return product_list



def products_from_cache():
    """Функция проверки, есть ли объекты в кэше"""
    if not CACHE_ENABLED: # Если кэширование не включено в проект, то возвр объекты из БД
        return Product.objects.all()

    key = 'product_list'
    products = cache.get(key)
    # если продукты есть в кэше, получаем из кэша
    if products is not None:
        return products

    # если продуктов нет в кэше, то добавляем их в кэш
    products = Product.objects.all()
    cache.set(key, products)
    return products