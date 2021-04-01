from django.forms import models
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Supervisor(models.Model):

    user = models.CharField(max_length=255, verbose_name='Пользователь',)
    phone = models.CharField(max_length=255, verbose_name='телефон')
    address = models.CharField(max_length=255, verbose_name='адресс')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')


    def __str__(self):
        return self.user
