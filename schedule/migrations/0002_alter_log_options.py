# Generated by Django 4.2.2 on 2024-05-13 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Лог', 'verbose_name_plural': 'Логи'},
        ),
    ]
