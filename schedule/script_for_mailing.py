from apscheduler.schedulers.background import BackgroundScheduler

from schedule.utils import create_daily_task, create_weekly_task, create_monthly_task


def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(create_daily_task, 'interval', seconds=10)
    scheduler.add_job(create_weekly_task, 'interval', seconds=10)
    scheduler.add_job(create_monthly_task, 'interval', seconds=10)
    scheduler.start()