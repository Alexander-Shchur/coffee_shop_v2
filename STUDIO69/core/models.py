from django.db import models


# Create your models here.
class AbstractProduct(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название'
    )

    icon = models.ImageField(
        verbose_name='Картинка'
    )

    price = models.ForeignKey(
        'Prices',
        on_delete=models.CASCADE,
        verbose_name='Цена'
    )


class Coffee(AbstractProduct):
    ROASTING_CHOICES = [
        ('Средняя', 'Средняя'),
        ('Темная', 'Темная')
    ]
    MILL_CHOICES = [
        ('Зерна', 'Зерна'),
        ('Мелкий', 'Мелкий')
    ]

    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        verbose_name='Страна'
    )

    roasting = models.CharField(
        max_length=12,
        choices=ROASTING_CHOICES,
        default='Средняя',
        verbose_name='Обжарка'
    )

    mill = models.CharField(
        max_length=12,
        choices=MILL_CHOICES,
        default='Зерна',
        verbose_name='Помол'
    )

    weight = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Вес'

    )


class Prices(models.Model):
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name='Цена'
    )


class Country(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название'
    )
