
from django.shortcuts import render


def home(requests):
    """Первый контроллер обработки страницы home.html"""
    return render(requests, 'home.html')


def contacts(requests):
    """Второй контроллер обработки страницы contacts.html"""
    return render(requests, 'contacts.html')


def get_contact(request):
    """Контроллерр обработки post запроса"""
    print("Начало работы контроллера")
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        print(f"Name: {name}, Message: {message}")
        return render(request, 'contacts.html', {'success_message': f"Спасибо, {name}, сообщение получено:"})
    # Этот ретерн на случай если был не пост запрос
    print("конец работы контроллера")
    return render(request, 'contacts.html')
