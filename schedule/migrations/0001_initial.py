# Generated by Django 4.2.2 on 2024-05-13 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.CharField(max_length=200, verbose_name='контактный email')),
                ('fullname', models.TextField(verbose_name='фио')),
                ('comment', models.CharField(max_length=250, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='TextForNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='тема')),
                ('text', models.TextField(verbose_name='текст')),
            ],
            options={
                'verbose_name': 'Текст для отправки',
                'verbose_name_plural': 'Тексты для рассылок',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='время начала рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='время окончания рассылки')),
                ('frequency', models.CharField(choices=[('Ежедневно', 'раз в день'), ('Еженедельно', 'раз в неделю'), ('Ежемесячно', 'раз в месяц')], max_length=300, verbose_name='Частота отправки')),
                ('status_of_newsletter', models.CharField(choices=[('Создать', 'Создана'), ('Запустить', 'Отправлено'), ('Завершить', 'Завершена')], max_length=150, verbose_name='статус рассылки')),
                ('clients', models.ManyToManyField(to='schedule.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.textfornewsletter', verbose_name='Сообщение для отправки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_attempt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='дата и время последней попытки')),
                ('status_of_last_attempt', models.BooleanField(blank=True, null=True, verbose_name='Статус попытки')),
                ('server_response', models.CharField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('clients_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.client', verbose_name='Клиенты для рассылки')),
                ('mailing_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.newsletter', verbose_name='Письма для рассылки')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылок',
            },
        ),
    ]
