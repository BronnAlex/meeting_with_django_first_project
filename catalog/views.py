from django.shortcuts import render
from catalog.models import Product, Contact

def home(request):
    """Первый контроллер обработки страницы home.html"""
    products = Product.objects.all().order_by('-created_at')  # Получаем все продукты из базы данных в порядке убывания по дате
    context = {'products': products[:5]}  # Создаем словарь с данными
    print(context)
    return render(request, "home.html", context)


def contacts(request):
    """Второй контроллер обработки страницы contacts.html,
    а также post  и get запросов"""

    print("Начало работы контроллера")

    # Условие обработки POST запроса
    if request.method == "POST":
        print("Начало работы POST запроса")

        name = request.POST.get("name")
        message = request.POST.get("message")
        print(f"Имя: {name}, сообщение: {message}")

        return render(
            request,
            "contacts.html",
            {"success_message": f"Спасибо, {name}, сообщение получено:"},
        )

    # Условие обработки GET запроса
    if request.method == "GET":
        contacts_company = Contact.objects.filter(name_country='Россия')  # Получаем все контакты
        context_contact = {'contacts_company': contacts_company}  # Создаем словарь с контактными данными
        print(context_contact)
        print("Начало работы GET запроса")

        return render(request, "contacts.html", context_contact)
