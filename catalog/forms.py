from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from .validators import (validate_forbidden_words, validate_image_size_5mb,
                         validate_image_type)

# вызываем функцию валидации плохих слов созданную нами
# not_valid_words = validate_forbidden_words()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name_product",
            "description_product",
            "photo_product",
            "category_product",
            "unit_price_product",
            "created_at",
        ]

    photo_product = forms.ImageField(
        validators=[validate_image_type, validate_image_size_5mb],
        label="Изображение",
        help_text="Загрузите изображение в формате JPEG или PNG (до 5 МБ).",
    )

    def clean_unit_price_product(self):
        unit_price_product = self.cleaned_data["unit_price_product"]
        if unit_price_product <= 0:
            raise ValidationError("Цена не может быть отрицательной или равной нулю")
        return unit_price_product

    def clean_name_product(self):
        """Валидация через функцию валидатор, которая имеет один обязательный арг"""
        name_product = self.cleaned_data["name_product"]
        validate_forbidden_words(name_product, "Слово {word} недопустимо в названии")
        return name_product

    def clean_description_product(self):
        """Валидация через функцию валидатор, которая имеет один обязательный арг"""
        description_product = self.cleaned_data["description_product"]
        validate_forbidden_words(
            description_product, "Слово {word} недопустимо в описании"
        )
        return description_product

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields["name_product"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите название продукта",  # Текст подсказки внутри поля
            }
        )

        self.fields["description_product"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Опишите продукт",  # Текст подсказки внутри поля
            }
        )

        self.fields["photo_product"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Загрузите фото продукта",  # Текст подсказки внутри поля
            }
        )

        self.fields["category_product"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Выберете категорию",  # Текст подсказки внутри поля
            }
        )

        self.fields["unit_price_product"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Укажите цену",  # Текст подсказки внутри поля
            }
        )

        self.fields["created_at"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Укажите дату создания",  # Текст подсказки внутри поля
            }
        )
