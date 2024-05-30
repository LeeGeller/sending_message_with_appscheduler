from django.contrib import admin

from schedule.models import Client, TextForNewsletter, Newsletter, Log


@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = (
        "pk",
        "contact_email",
        "fullname",
        "comment",
    )


@admin.register(TextForNewsletter)
class TextForNewsletter(admin.ModelAdmin):
    list_display = (
        "pk",
        "subject",
        "text",
    )


@admin.register(Newsletter)
class Newsletter(admin.ModelAdmin):
    list_display = (
        "pk",
        "start_time",
        "end_time",
        "frequency",
        "status_of_newsletter",
    )


@admin.register(Log)
class Log(admin.ModelAdmin):
    list_display = (
        "pk",
        "status_of_last_attempt",
        "server_response",
        "time_attempt",
    )
