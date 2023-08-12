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
