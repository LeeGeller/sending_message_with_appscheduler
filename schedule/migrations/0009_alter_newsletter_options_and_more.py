# Generated by Django 4.2.2 on 2024-05-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0008_client_company_log_company_textfornewsletter_company"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newsletter",
            options={
                "permissions": [
                    ("can_view_newsletter", "Может видеть все рассылки"),
                    ("can_disable_newsletter", "Может отключать рассылки"),
                    (
                        "cannot_manage_newsletter_list",
                        "Не может управлять списком рассылок",
                    ),
                    ("cannot_change_newsletter_list", "Не может изменять рассылки"),
                ],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.AlterModelOptions(
            name="textfornewsletter",
            options={
                "permissions": [
                    (
                        "cannot_change_textfornewsletter_list",
                        "Не может изменять текст для рассылок",
                    )
                ],
                "verbose_name": "Текст для отправки",
                "verbose_name_plural": "Тексты для рассылок",
            },
        ),
    ]
