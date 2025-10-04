from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("catalog.urls", namespace="catalog")
    ),  # Путь к нашему приложению catalog
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)
