from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=50, verbose_name="Email", help_text="Введите свой email", unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
