from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, verbose_name="Email", unique=True)
    company = models.CharField(max_length=200, verbose_name="Компания", null=True)
    token = models.CharField(
        max_length=200, verbose_name="Token", blank=True, null=True
    )
    is_active = models.BooleanField(default=False)
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="users/", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
