from django_cron import CronJobBase, Schedule

from schedule.utils import get_print


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Задать периодичность выполнения

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'schedule.utils.get_print'  # Функция, которая будет запускаться

    def do(self):
        # Код, который будет выполнен при запуске
        get_print()
