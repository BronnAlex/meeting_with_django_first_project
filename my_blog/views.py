from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from my_blog.models import BlogEntry


# CRUD
class MyBlogListView(ListView):
    # Создается шаблон либо явно либо автоматически
    # Шаблон как правило наследуется от base.html. Также подгружаются собственные тэги(обычно фильтрации) в base.
    # Для отображения фотографий на сайте
    template_name = "my_blog/blogentry_list.html"
    model = BlogEntry

    def get_context_data(self, **kwargs):
        # Передача нужных данных (рендеринг) из БД в шаблон. Дальше перебирается циклом
        # Также идет фильтрация по положительному признаку публикации(все работает)
        context = super().get_context_data(**kwargs)
        context["blog_data"] = BlogEntry.objects.filter(is_active=True).order_by("id")[
            :3
        ]  # лучше сортировать по дате с часами, сейчас часов нет
        context["top_two_post"] = BlogEntry.objects.filter(is_active=True).order_by(
            "-id"
        )[:2]
        context["all_data"] = BlogEntry.objects.filter(is_active=True)
        return context

    # На данный момент работает


class MyBlogDetailView(DetailView):
    # Создается отдельный шаблон с данными об объекте
    # Обращение к объекту происходит через переменную object {{ object.preview_image | media_filter_blog }}
    model = BlogEntry
    template_name = "my_blog/blogentry_detail.html"

    def get_object(self, queryset=None):
        # получение объекта из кверисета и увеличение счетчика при просмотре
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class MyBlogCreateView(CreateView):
    # необходимо создать html шаблон с формой
    # разместить кнопку в списках или где-то еще для перехода на форму
    # Перенаправление после успешного создания
    model = BlogEntry
    fields = ("title", "content", "preview_image", "is_active", "count_views")
    template_name = "my_blog/blogentry_form.html"
    success_url = reverse_lazy("my_blog:my_blog_list")


class MyBlogUpdateView(UpdateView):
    # Отдельный шаблон не создается. Автоматически переходит на форму создания(create) для изменения данных
    # разместить кнопку необходимо рядом с тем товаром, который надо изменить.
    # также добавить маршрут с pk как правило все это в цикле
    # Перенаправление после успешного обновления
    model = BlogEntry
    fields = ("title", "content", "preview_image", "is_active", "count_views")
    success_url = reverse_lazy("my_blog:my_blog_list")

    def get_success_url(self):

        return reverse("my_blog:my_blog_detail", args=[self.kwargs.get("pk")])


class MyBlogDeleteView(DeleteView):
    # Создается отдельный шаблон похожий на создание,
    # так как кто-то мог случано нажать удалить и надо подтверждение
    # Перенаправление после успешного удаления либо отмены
    model = BlogEntry
    template_name = "my_blog/blogentry_confirm_delete.html"
    success_url = reverse_lazy("my_blog:my_blog_list")
