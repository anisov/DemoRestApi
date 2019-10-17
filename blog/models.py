from django.db import models
from django.contrib.auth import get_user_model
from cars.models import Car

User = get_user_model()


class Blog(models.Model):
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='Машина', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Блог'
        ordering = ['id']
