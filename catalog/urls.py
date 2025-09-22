from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts  # get_contact  # импорт функций это наши контроллеры

app_name = CatalogConfig.name  # Это и будет наше имя приложения, оно зафиксировано при создании в классе CatalogConfig

urlpatterns = [
    # Путь admin/ из config/urls.py чтобы сразу отображалась страница каталог
    path('', home, name=app_name),
    # чтобы отображалась страница каталог при нажатии на кнопку каталог со страницы контактов,
    # а также на самой странице каталога также добавил это в html шаблоне
    path('home/', home, name=app_name),
    # Путь чтобы отображалась страница контактов при переходе с каталога,
    # также добавил это в html шаблоне и обработка POST и GET запросов
    path('contacts/', contacts, name=app_name),
    # переменную name можно называть как угодно для идентификации маршрута. И чтобы команде было понятно

]
