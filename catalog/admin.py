from django.contrib import admin
from .models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_product",
        "unit_price_product",
    )
    list_filter = ("category_product",)
    search_fields = (
        "name_product",
        "description_product",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_category",
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (

        "name_country",
        'inn_company',
        'adr_contact',
    )


# Настройте отображение для моделей:
# Для Category выведите id и name в списке.
# Для Product выведите id, name, price и category в списке.
# Настройте фильтрацию продуктов по категории.
# Настройте поиск по полям name и description
