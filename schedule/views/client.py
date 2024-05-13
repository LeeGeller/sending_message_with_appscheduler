from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from schedule.models import Client


class ClientsListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('contact_email', 'fullname', 'comment',)
    success_url = reverse_lazy("schedule:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('contact_email', 'fullname', 'comment',)

    def get_success_url(self):
        return reverse("schedule:client_list")


class ClientDeleteView(DeleteView):
    model = Client

    def get_success_url(self):
        return reverse("schedule:client_list")
