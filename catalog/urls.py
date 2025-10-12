from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from catalog.views import (
    home,
    contacts,
    product_details,
)

app_name = "catalog"

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product_details/<int:pk>/", product_details, name="product_details"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
