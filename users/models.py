from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        max_length=50, verbose_name="Email", help_text="Введите свой email", unique=True
    )
    company = models.CharField(max_length=200, verbose_name="", null=True)
    token = models.CharField(max_length=200, verbose_name="Token", blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
