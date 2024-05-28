from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from config import settings
from users.apps import UserConfig
from users.services import email_verification
from users.views import UserCreateView, PasswortResetView

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('passwort_reset_view/', PasswortResetView.as_view(), name='passwort_reset'),
    path(
        "confirm-register/<str:token>/",
        email_verification,
        name="confirm-register",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
