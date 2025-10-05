from django.db import models


class Category(models.Model):
    """Модель Категории"""

    # Поля модели
    name_category = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Название Категории"
    )
    description_category = models.TextField(
        verbose_name="Описание", help_text="Описание категории"
    )

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name_category",
        ]


class Product(models.Model):
    """Модель продуктов"""

    # Поля модели
    name_product = models.CharField(
        max_length=100, verbose_name="Продукт", help_text="Название продукта"
    )
    description_product = models.TextField(
        verbose_name="Описание", help_text="Описание продукта"
    )
    photo_product = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category_product = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию",
        null=True,
        blank=True,
        related_name="products",
    )
    unit_price_product = models.IntegerField(help_text="Цена за покупку")
    created_at = models.DateField(
        verbose_name="Дата создания", help_text="Введите дату создания продукта"
    )
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name_product", "unit_price_product", "created_at", "updated_at"]


class Contact(models.Model):
    """Модель контактов"""

    # Поля модели
    name_country = models.CharField(
        max_length=100, verbose_name="Контакт", help_text="Страна"
    )
    inn_company = models.TextField(
        verbose_name="Описание", help_text="Инн компании"
    )

    adr_contact = models.TextField(
        verbose_name="Номер", help_text="Адрес компании и телефон"
    )

    def __str__(self):
        return self.name_country

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = [
            "name_country",
        ]