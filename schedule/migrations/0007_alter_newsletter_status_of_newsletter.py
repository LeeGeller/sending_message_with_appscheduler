# Generated by Django 4.2.2 on 2024-05-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_alter_log_options_remove_log_clients_list_log_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='status_of_newsletter',
            field=models.CharField(choices=[('Создана', 'Создана'), ('Отправлено', 'Запущена'), ('Завершена', 'Завершена'), ('Ошибка отправки', 'Ошибка отправки')], max_length=150, verbose_name='статус рассылки'),
        ),
    ]
