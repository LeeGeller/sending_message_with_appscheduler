# Generated by Django 4.2.2 on 2024-05-30 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0011_alter_newsletter_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newsletter",
            options={"verbose_name": "Рассылка", "verbose_name_plural": "Рассылки"},
        ),
    ]
