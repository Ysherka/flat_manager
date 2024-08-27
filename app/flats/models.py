from django.db import models


class Flat(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.IntegerField(default=0, verbose_name='Цена')
    longitude = models.FloatField(default=0, verbose_name='Долгота')
    latitude = models.FloatField(default=0, verbose_name='Широта')
    # owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Владелец')
    # 'booked_dates' in the app 'bookings'
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Рейтинг квартиры')

    def __str__(self):
        return f'{self.title} <{self.pk}>'

    def get_main_img(self):
        if FlatImage.objects.filter(flat=self.pk).first():
            main_img = FlatImage.objects.filter(flat=self.pk).first().image
            return main_img
        else:
            return None

    def get_reviews(self):
        reviews = FlatReview.objects.filter(flat=self.pk)
        if reviews:
            return reviews
        else:
            return None


def get_flat_images_path(flat_obj, filename: str):
    if FlatImage.objects.last():
        last_img_id = FlatImage.objects.last().id
    else:
        last_img_id = 0
    new_filename = str(last_img_id + 1) + '.' + filename.split('.')[-1]
    return f'flats_images/{flat_obj.flat_id}/{new_filename}'

class FlatImage(models.Model):
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, verbose_name='Квартира')
    image = models.ImageField(upload_to=get_flat_images_path, verbose_name='Изображение квартиры')




class FlatReview(models.Model):
    # author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор отзыва')
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, verbose_name='Квартира с отзывом')
    text = models.TextField(max_length=500, verbose_name='Текст отзыва')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, verbose_name='Рейтинг отзыва')