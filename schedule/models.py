

from django.db import models

CREATE = 'Создана'
STARTED = 'Отправлено'
DONE = 'Завершена'

DAILY = 'раз в день'
WEEKLY = 'раз в неделю'
MONTHLY = 'раз в месяц'

FREQUENCY_CHOICES = [('Ежедневно', DAILY), ('Еженедельно', WEEKLY), ('Ежемесячно', MONTHLY), ]
STATUS_OF_NEWSLETTER = [("Создать", CREATE), ("Запустить", STARTED), ("Завершить", DONE), ]


class Client(models.Model):
    contact_email = models.CharField(max_length=200, verbose_name='контактный email')
    fullname = models.TextField(verbose_name='фио')
    comment = models.CharField(max_length=250, verbose_name='комментарий')

    def __str__(self):
        return f"{self.contact_email} {self.fullname} {self.comment}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TextForNewsletter(models.Model):
    subject = models.CharField(max_length=200, verbose_name='тема')
    text = models.TextField(verbose_name='текст')

    def __str__(self):
        return f"{self.subject} {self.text}"

    class Meta:
        verbose_name = "Текст для отправки"
        verbose_name_plural = "Тексты для рассылок"


class Newsletter(models.Model):
    start_time = models.DateTimeField(verbose_name='время начала рассылки', blank=True, null=True)
    end_time = models.DateTimeField(verbose_name='время окончания рассылки', blank=True, null=True)
    frequency = models.CharField(max_length=300, choices=FREQUENCY_CHOICES, verbose_name="Частота отправки")
    status_of_newsletter = models.CharField(max_length=150, verbose_name='статус рассылки',
                                            choices=STATUS_OF_NEWSLETTER)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    message = models.ForeignKey(TextForNewsletter, on_delete=models.CASCADE, verbose_name='Сообщение для отправки')

    def __str__(self):
        return f"{self.start_time} {self.end_time} {self.frequency} {self.status_of_newsletter} {self.clients} {self.message}"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Log(models.Model):
    time_attempt = models.DateTimeField(verbose_name='дата и время последней попытки', auto_now_add=True, blank=True,
                                        null=True)
    status_of_last_attempt = models.BooleanField(verbose_name='Статус попытки', blank=True,
                                                 null=True)

    clients_list = models.ManyToManyField(Client, verbose_name='Клиенты для рассылки', blank=True,
                                     null=True)
    mailing_list = models.ManyToManyField(Newsletter, verbose_name='Письма для рассылки',
                                     blank=True,
                                     null=True)

    server_response = models.CharField(verbose_name='Ответ почтового сервера', max_length=255, blank=True, null=True)

    def __str__(self):
        return f" {self.status_of_last_attempt} {self.clients_list} {self.mailing_list} {self.server_response} {self.time_attempt}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"

