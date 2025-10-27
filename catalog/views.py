from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Contact, Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):

        product = form.save(form)  # сохраняем продукт
        # user = self.request.user
        # product.owner = user  Данный код не актуален, так как происходит два запроса к БД
        form.instance.owner = self.request.user # одним запросом заполняются данные в БД
        product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
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
