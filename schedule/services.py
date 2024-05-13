from datetime import datetime
from smtplib import SMTPException

import pytz
from django.conf import settings
from django.core.mail import send_mail

from schedule.models import Log, DONE


def send_mailing(mailing):
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    # создание объекта с применением фильтра
    if mailing.start_time <= current_datetime <= mailing.end_time:
        for message in mailing.message:
            for client in mailing.clients.all():
                try:
                    result = send_mail(
                        subject=message.subject,
                        message=message.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )
                    log = Log.objects.create(
                        time_attempt=mailing.start_time,
                        status_of_last_attempt=result,
                        server_response='OK',
                        mailing_list=mailing,
                        clients_list=client
                    )
                    log.save()

                    return log
                except SMTPException as error:
                    log = Log.objects.create(
                        time_attempt=mailing.start_time,
                        status_of_last_attempt=False,
                        server_response=error,
                        mailing_list=mailing,
                        clients_list=client
                    )
                    log.save()
                return log
            else:
                mailing.status_of_newsletter = DONE
                mailing.save()
