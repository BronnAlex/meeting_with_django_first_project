from django import template

# Описание шаблонного фильтра
register = template.Library()


@register.filter()
def media_filter(path):
    print(f" Путь {path}")
    if path:
        return f"/media/{path}"
    return "#"


# Шаблонный фильтр для svg
# Прописал для поиска пути фото в формате svg, как применить пока что не знаю.
# Так как подгрузка данного тега происходит к моели и его полю, а мне надо просто фото лого находящегося в корне проекта
@register.filter()
def brand_svg(path):
    print(f" Путь svg {path}")
    if path:
        return f"/media/{path}"
    return "#"
