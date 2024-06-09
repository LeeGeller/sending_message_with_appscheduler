from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from schedule.crontab import do

        do()
