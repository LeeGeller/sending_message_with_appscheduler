from schedule.models import Newsletter, DAILY, CREATE, WEEKLY, MONTHLY
from schedule.services import send_mailing


def create_daily_task():
    mailings = Newsletter.objects.filter(frequency=DAILY, status_of_newsletter=CREATE)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def create_weekly_task():
    mailings = Newsletter.objects.filter(frequency=WEEKLY, status_of_newsletter=CREATE)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def create_monthly_task():
    mailings = Newsletter.objects.filter(frequency=MONTHLY, status_of_newsletter=CREATE)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)
