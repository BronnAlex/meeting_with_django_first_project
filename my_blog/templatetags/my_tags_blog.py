from django import template

# Описание шаблонного фильтра
register = template.Library()


@register.filter()
def media_filter_blog(path):
    print(f" Путь фото блога {path}")
    if path:
        return f"/media/{path}"
    return "#"



