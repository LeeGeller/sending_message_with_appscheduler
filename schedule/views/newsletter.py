from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from schedule.forms import NewsletterForm
from schedule.models import Newsletter, CREATE, Client, TextForNewsletter
from schedule.services import send_mailing
import logging


class NewsletterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Newsletter
    permission_required = "schedule.can_view_newsletter"

    def get_queryset(self):
        user = self.request.user
        company = user.user_company

        if user.has_perm("schedule.can_view_newsletter") or user.is_superuser:
            return Newsletter.objects.all()

        newsletters = (
            Newsletter.objects.filter(clients__company=company)
            .prefetch_related("clients__company", "message")
            .distinct()
        )
        return newsletters


class NewsletterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    permission_required = "schedule.cannot_change_newsletter_list"

    success_url = reverse_lazy("schedule:newsletter_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        company = user.user_company

        if not user.has_perm("schedule.cannot_change_newsletter_list"):
            form.fields["clients"].queryset = Client.objects.filter(company=company)
            form.fields["message"].queryset = TextForNewsletter.objects.filter(
                company=company
            )
            return form
        else:
            return HttpResponseForbidden("Go out!")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_messages = form.cleaned_data.get("message")
        selected_start_time = form.cleaned_data.get("start_time")

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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        user = self.request.user
        company = user.user_company

        form.fields["clients"].queryset = Client.objects.filter(company=company)
        form.fields["message"].queryset = TextForNewsletter.objects.filter(
            company=company
        )
        return form

    def get_success_url(self):
        return reverse("schedule:newsletter_list")

    def form_valid(self, form):
        newsletter = form.save(commit=False)

        selected_clients = form.cleaned_data.get("clients")
        selected_messages = form.cleaned_data.get("message")
        selected_start_time = form.cleaned_data.get("start_time")

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
