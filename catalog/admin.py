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
        "inn_company",
        "adr_contact",
    )
