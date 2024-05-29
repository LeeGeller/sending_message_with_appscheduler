# Generated by Django 4.2.2 on 2024-05-29 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_company_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(max_length=150, verbose_name="Название компании"),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="company",
        ),
        migrations.AddField(
            model_name="user",
            name="user_company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
    ]
