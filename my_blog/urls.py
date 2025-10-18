from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from my_blog.views import (
    MyBlogListView,
    MyBlogDetailView,
    MyBlogCreateView,
    MyBlogUpdateView,
    MyBlogDeleteView,
)

app_name = "my_blog"

urlpatterns = [
    path("", MyBlogListView.as_view(), name="my_blog_list"),
    path("detail/<int:pk>/", MyBlogDetailView.as_view(), name="my_blog_detail"),
    path("create/", MyBlogCreateView.as_view(), name="my_blog_create"),
    path("<int:pk>/update/", MyBlogUpdateView.as_view(), name="my_blog_update"),
    path("<int:pk>/delete/", MyBlogDeleteView.as_view(), name="my_blog_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documment_root=settings.MEDIA_ROOT)
