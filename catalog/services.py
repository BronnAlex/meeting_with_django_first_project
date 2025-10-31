from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

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