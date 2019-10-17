from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin_name_regex = RegexValidator(regex=r"^[0-9A-ZА-ЯЁ\- ]{1,17}$",
                                    message='Поле "Идентификационный номер VIN/Рама" заполнено неверно.')
    vin = models.CharField(verbose_name='Vin', unique=True, validators=(RegexValidator,),
                           db_index=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64)
    brand = models.CharField(verbose_name='Брэнд', max_length=64)
    GENDER_CHOICES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),

    )
    car_type = models.IntegerField(verbose_name='Тип Машины', choices=GENDER_CHOICES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
