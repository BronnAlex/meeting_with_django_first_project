from django.contrib import admin

from catalog.models import Category, Contact, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс регистрации модели продуктов в админке"""

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
    """Класс регистрации модели категории продуктов в админке"""

    list_display = (
        "id",
        "name_category",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Класс регистрации модели контактов компании в админке"""

    list_display = (
        "name_country",
        "inn_company",
        "adr_contact",
    )
