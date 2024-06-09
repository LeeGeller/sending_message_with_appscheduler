from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "schedule"


# Чтобы cromtab работал при запуске приложений, нужно будет его раскомитить
# def ready(self):
#     from schedule.crontab import do
#
#     do()
