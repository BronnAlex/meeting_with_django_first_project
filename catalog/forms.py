from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'description_product', 'photo_product', 'category_product', 'unit_price_product', 'created_at']
