from django.contrib.auth.forms import UserCreationForm
from django import forms

from schedule.forms import MixinForms
from users.models import User


class UsersRegisterForm(MixinForms, UserCreationForm):
    class Meta:
        model = User

        fields = (
            "email",
            "company",
            "password1",
            "password2",
        )

