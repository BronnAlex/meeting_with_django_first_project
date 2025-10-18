from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
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
class MyBlogCreateView(CreateView):
    model = BlogEntry
    fields = ('title', 'content', 'preview_image', 'is_active', 'count_views')
    template_name = 'my_blog/blogentry_form.html'
    success_url = reverse_lazy('my_blog:my_blog_list')

