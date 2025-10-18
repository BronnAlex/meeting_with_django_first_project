from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product, Contact


class CatalogListView(ListView):
    model = Product

    # app_name/model_action - поиск шаблона по умолчанию
    # catalog/product_list.html
    # Ранее мы записывали QuerySet в context, теперь он создается по умолчаию как object_action(object_list)


class CatalogTemplateView(TemplateView):
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


class CatalogDetailView(DetailView):
    model = Product

    # app_name/model_action - поиск шаблона по умолчанию
    # catalog/product_detail.html
    # Ранее мы записывали QuerySet в context, теперь он создается по умолчанию как object_action(object_detail)
