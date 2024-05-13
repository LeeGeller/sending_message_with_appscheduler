from time import sleep

from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedule'

    def ready(self):
        from schedule.script_for_mailing import start
        sleep(2)
        start()
