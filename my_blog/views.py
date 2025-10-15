from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from my_blog.models import BlogEntry


class MyBlogListView(ListView):
    model = BlogEntry
    # На данный момент работает

    # app_name/model_action - поиск шаблона по умолчанию
    # catalog/product_list.html

# def home(request):
#     """Первый контроллер обработки страницы home.html"""
#     products = (
#         BlogEntry.objects.all()
#     )  # Получаем все продукты из базы данных в порядке убывания по дате
#     context = {"products": products}  # Создаем словарь с данными
#
#     return render(request, "my_blog/blogentry_list.html", context)