from django.urls import reverse
from django.views.generic import ListView

from schedule.models import Log


class LogListView(ListView):
    model = Log

    def get_success_url(self):
        return reverse("schedule:log_list")

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        return context_data
