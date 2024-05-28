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


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Email", max_length=254, help_text="Введите email для отправки"
    )
