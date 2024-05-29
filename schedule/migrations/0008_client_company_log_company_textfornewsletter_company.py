# Generated by Django 4.2.2 on 2024-05-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_company_remove_user_company_user_user_company"),
        ("schedule", "0007_alter_newsletter_status_of_newsletter"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
        migrations.AddField(
            model_name="textfornewsletter",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.company",
                verbose_name="Компания",
            ),
        ),
    ]
