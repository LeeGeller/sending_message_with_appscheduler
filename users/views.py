import secrets

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import DEFAULT_FROM_EMAIL
from users.form import UsersRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UsersRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.token = secrets.token_hex(16)
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/confirm-register/{user.token}/"

        send_mail(subject="Hi! You need to confirm your registrations",
                  message=f"Clicke here if it was you: {url}",
                  from_email=DEFAULT_FROM_EMAIL,
                  recipient_list=[user.email])

        return super().form_valid(form)


class PasswortResetView(UserCreateView):
    model = User
    template_name = "password_reset.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        email_form = form.cleaned_data('email')
        user = User.objects.get(email=email_form)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(subject="New password",
                  message=f"Here: {new_password}",
                  from_email=DEFAULT_FROM_EMAIL,
                  recipient_list=[user.email])
        return super().form_valid(form)