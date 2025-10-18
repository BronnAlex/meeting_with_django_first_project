from django.views.generic import ListView, DetailView, TemplateView
from my_blog.models import BlogEntry

# CRUD
class MyBlogListView(ListView):
    template_name = 'my_blog/blogentry_list.html'
    model = BlogEntry
    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['blog_data'] = BlogEntry.objects.all().order_by('id')[:3] # лучше сортировать по дате с часами, сейчас часов нет
        context['top_two_post'] = BlogEntry.objects.all().order_by('-id')[:2]
        context['all_data'] = BlogEntry.objects.all()
        return context
    # На данный момент работает


class MyBlogDetailView(DetailView):
    model = BlogEntry
    template_name = 'my_blog/blogentry_detail.html'



    # app_name/model_action - поиск шаблона по умолчанию
    # catalog/product_list.html


# def detail(request):
#     blog_data = BlogEntry.objects.all()
#     context = {"blogs": blog_data}
#     print(context)
#     return render(request, "my_blog/base.html", context)

