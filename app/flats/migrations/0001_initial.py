# Generated by Django 5.1 on 2024-08-22 13:01

import django.db.models.deletion
import flats.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Рейтинг квартиры')),
            ],
        ),
        migrations.CreateModel(
            name='FlatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=flats.models.get_flat_images_path, verbose_name='Изображение квартиры')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.flat', verbose_name='Квартира')),
            ],
        ),
        migrations.CreateModel(
            name='FlatReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='Рейтинг отзыва')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flats.flat', verbose_name='Квартира с отзывом')),
            ],
        ),
    ]
