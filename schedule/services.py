from datetime import datetime
from random import shuffle
from smtplib import SMTPException

import pytz
from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.shortcuts import redirect

from blog.models import Blog
from schedule.models import Log, DONE, ERROR, Newsletter, STARTED


def send_mailing(mailing):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    current_time_formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S%z")
    time_obj = datetime.strptime(current_time_formatted, "%Y-%m-%d %H:%M:%S%z")

    # Проверяем, должна ли рассылка выполняться в данный момент времени
    if mailing.start_time >= time_obj <= mailing.end_time:
        try:
            for client in mailing.clients.all():
                for post in mailing.message.all():
                    result = send_mail(
                        subject=post.subject,
                        message=post.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.contact_email],
                        fail_silently=False,
                    )
                    # Создаем объект Log для записи в журнал
                    log = Log.objects.create(
                        time_attempt=current_datetime,
                        status_of_last_attempt=bool(result),
                        server_response="OK" if result else "Error",
                        mailing_list=mailing,
                        client=client,
                    )
                    log.save()

        except SMTPException as error:
            # Если произошла ошибка при отправке, создаем объект Log с соответствующими данными
            log = Log.objects.create(
                time_attempt=current_datetime,
                status_of_last_attempt=False,
                server_response=str(error),
                mailing_list=mailing,
            )
            log.save()
        mailing.status_of_newsletter = DONE
    if mailing.status_of_newsletter != DONE:
        mailing.status_of_newsletter = ERROR
    mailing.save()


def toggle_activity(request, pk):
    mailing = Newsletter.objects.get(pk=pk)
    if mailing.is_active:
        mailing.is_active = False
    else:
        mailing.is_active = True

    mailing.save()
    return redirect("schedule:newsletter_list")
