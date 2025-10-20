from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),  # Путь к приложению catalog
    path(
        "blogs/", include("my_blog.urls", namespace="my_blog")
    ),  # Путь к приложению my_blog
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)
