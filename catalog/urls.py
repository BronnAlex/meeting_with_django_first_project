from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from catalog.views import CatalogListView, CatalogDetailView, CatalogTemplateView

app_name = "catalog"

urlpatterns = [
    path("", CatalogListView.as_view(), name="product_list"),
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path("contacts/", CatalogTemplateView.as_view(), name="contacts"),
    # path("product_details/<int:pk>/", product_details, name="product_details"),
    path(
        "product_detail/<int:pk>/", CatalogDetailView.as_view(), name="product_detail"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
