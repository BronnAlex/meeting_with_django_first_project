from django.shortcuts import render


def home(request):
    """Первый контроллер обработки страницы home.html"""
    return render(request, "home.html")


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
        print("Начало работы GET запроса")

        return render(request, "contacts.html")
