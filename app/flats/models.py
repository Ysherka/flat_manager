from django.db import models

from .utils import get_flat_images_path

class Flat(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.IntegerField(default=0, verbose_name='Цена')
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Владелец')
    # 'booked_dates' in the app 'bookings'
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг квартиры')


class Image(models.Model):
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, verbose_name='Квартира')
    image = models.ImageField(upload_to=get_flat_images_path, verbose_name='Изображение квартиры')


class Review(models.Model):
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор отзыва')
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, verbose_name='Квартира с отзывом')
    text = models.TextField(max_length=500, verbose_name='Текст отзыва')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, verbose_name='Рейтинг отзыва')