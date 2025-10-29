from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Contact, Product


class ProductListView(ListView):
    """Класс представления списка продуктов в шаблоне"""

    model = Product
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    """Класс детального представления продукта в шаблоне"""

    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(CreateView, LoginRequiredMixin):
    """Класс создания нового списка продукта в шаблоне с формой"""

    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        """Метод изменения поля модели при создании продукта"""
        product = form.save(commit=False)  # отсроченное сохранение продукта
        # user = self.request.user
        # product.owner = user  Данный код не актуален, так как происходит два запроса к БД
        form.instance.owner = (
            self.request.user
        )  # одним запросом заполняются данные в БД
        product.is_publicate = (
            True  # Изменение статуса публикации при создании продукта
        )
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс обновления и редактирования конкретного продукта"""

    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        """Метод проверки валидации"""
        return super().form_valid(form)

    def get_form_class(self):
        """Метод проверки прав пользователя"""
        user = self.request.user
        if user == self.object.owner:  # Если пользователь является собственником
            return ProductForm

        if user.has_perm(
            "catalog.can_unpublish_product"
        ):  # Если пользователь Имеет кастомные права
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    """Класс удаления  продукта в шаблоне"""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        """Метод проверки прав пользователя при удалении продукта"""
        user = self.request.user
        if (
            user == self.object.owner
        ):  # Если пользователь является собственником, то тогда может удалять
            return ProductForm
        raise PermissionDenied


class ContactTemplateView(TemplateView):
    """Класс представления контактов компании в шаблоне"""

    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        """Метод переопределения данных если они не заданы"""
        context = super().get_context_data(**kwargs)
        try:
            company_info = Contact.objects.first()  # Получите первую запись из модели
            context["company_name"] = company_info.name_country
            context["inn_company"] = company_info.inn_company
            context["adr_contact"] = company_info.adr_contact
        except Contact.DoesNotExist:
            context["company_name"] = "Компания не найдена"
            context["description"] = "Информация о компании отсутствует."
            context["adr_contact"] = "Адрес отсутствует"

        return context
