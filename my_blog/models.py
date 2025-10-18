from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите название заголовка"
    )
    content = models.TextField(
        verbose_name="Контент", help_text="Напишите свой контент", null=True, blank=True
    )
    preview_image = models.ImageField(
        upload_to="my_blog/photo",
        verbose_name="Фото превью",
        help_text="Добавьте изображение",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания блога",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    count_views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовоки"
        ordering = [
            "title",
            "created_at",
        ]
