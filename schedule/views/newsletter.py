from django.utils import timezone

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from schedule.forms import NewsletterForm
from schedule.models import Newsletter, Log


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get('clients')
        newsletter.save()
        newsletter.clients.clear()

        for client in selected_clients:
            newsletter.clients.add(client)

        Log.objects.create(
            time_attempt=timezone.now(), status_of_last_attempt=False,
            clients_list=selected_clients, mailing_list=newsletter.message,
            server_response='OK'
        )

        # Возвращаем успешный ответ
        return super().form_valid(form)


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        return reverse("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get('clients')
        newsletter.save()
        newsletter.clients.clear()

        for client in selected_clients:
            newsletter.clients.add(client)

        current_datetime = timezone.now()

        # Создаем список клиентов для рассылки
        clients_list = list(selected_clients)

        # Создаем запись лога для всех клиентов
        Log.objects.create(
            time_attempt=current_datetime,
            status_of_last_attempt=False,
            server_response='OK',
        ).clients_list.set(clients_list)

        return super().form_valid(form)


class NewsletterDeleteView(DeleteView):
    model = Newsletter

    def get_success_url(self):
        return reverse("schedule:newsletter_list")
