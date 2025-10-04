from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig

name_space = CatalogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("catalog.urls", namespace=name_space)
    ),  # Путь к нашему приложению catalog
]
