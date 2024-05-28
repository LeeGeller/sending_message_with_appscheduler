from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UsersRegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = ('email', 'company', 'password1',
                  'password2',)
