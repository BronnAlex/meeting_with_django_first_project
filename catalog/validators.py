from django.core.exceptions import ValidationError
from PIL import Image


def validate_image_type(image):
    """Функция валидатор, которая проверяет, что файл соответствует нужному формату"""
    try:
        img = Image.open(image)
        if img.format not in ["JPEG", "PNG"]:
            raise ValidationError("Поддерживаются только файлы JPEG и PNG.")
    except Exception:
        raise ValidationError(
            "Не удалось определить формат изображения. Убедитесь, что файл является допустимым изображением."
        )


def validate_image_size_5mb(image):
    """
    Функция валидатор для проверки размера файла, что размер файла не превышает 5 МБ.
    """
    if (
        not image
    ):  # Проверка на случай, если поле необязательное и не было загружено файла
        return

    # 5 MB = 5 × 1024 × 1024 байт
    max_size = 5 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(
            f"Размер файла не должен превышать {max_size / (1024*1024):.0f} МБ."
        )


def validate_words():
    """Функция валидатор на запрещенные слова"""
    not_valid_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    return not_valid_words
