from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from my_blog.views import  MyBlogListView

app_name = "my_blog"

urlpatterns = [
    # path("", home, name='home'),
    path("", MyBlogListView.as_view(), name='my_blog_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)