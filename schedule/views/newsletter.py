from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from schedule.forms import NewsletterForm
from schedule.models import Newsletter, CREATE
from schedule.services import send_mailing
import logging



class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm

    success_url = reverse_lazy("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get('clients')
        selected_messages = form.cleaned_data.get('message')
        selected_start_time = form.cleaned_data.get('start_time')

        newsletter.status_of_newsletter = CREATE
        newsletter.start_time = selected_start_time

        newsletter.save()

        newsletter.clients.set(selected_clients)
        newsletter.message.set(selected_messages)

        send_mailing(newsletter)

        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    def get_success_url(self):
        return reverse("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get('clients')
        selected_messages = form.cleaned_data.get('message')
        selected_start_time = form.cleaned_data.get('start_time')

        newsletter.clients.clear()
        newsletter.message.clear()

        newsletter.clients.set(selected_clients)
        newsletter.message.set(selected_messages)

        newsletter.status_of_newsletter = CREATE
        newsletter.start_time = selected_start_time

        newsletter.save()

        send_mailing(newsletter)

        return super().form_valid(form)


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter

    def get_success_url(self):
        return reverse("schedule:newsletter_list")
