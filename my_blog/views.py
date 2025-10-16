from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from my_blog.models import BlogEntry


class MyBlogListView(ListView):
    model = BlogEntry
    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['blog_data'] = BlogEntry.objects.all().order_by('-id')[:3] # лучше сортировать по дате с часами, сейчас часов нет
        return context
    # На данный момент работает

    # app_name/model_action - поиск шаблона по умолчанию
    # catalog/product_list.html


# def detail(request):
#     blog_data = BlogEntry.objects.all()
#     context = {"blogs": blog_data}
#     print(context)
#     return render(request, "my_blog/base.html", context)

