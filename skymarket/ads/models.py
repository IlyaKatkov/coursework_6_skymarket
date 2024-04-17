from django.conf import settings
from django.db import models




NULLABLE = {'blank': True, 'null': True}
class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=100, **NULLABLE, verbose_name='название товара')
    price = models.PositiveIntegerField(default=1000, verbose_name='цена товара')
    description = models.CharField(max_length=200, **NULLABLE, verbose_name='описание товара')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(max_length=200, verbose_name='текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Создатель отзыва')
    ad = models.ForeignKey(Ad, on_delete=models.SET_NULL, **NULLABLE, verbose_name='объявление, под которым оставлен отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания отзыва')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
