# Generated by Django 4.2.2 on 2024-05-30 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name": "Компания", "verbose_name_plural": "Компании"},
        ),
    ]
