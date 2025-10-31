from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import (
    CategoryAndProductsListView,
    ContactTemplateView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path(
        "category_and_products/",
        CategoryAndProductsListView.as_view(),
        name="category_and_products",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
