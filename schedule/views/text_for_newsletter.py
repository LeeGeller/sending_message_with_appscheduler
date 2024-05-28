from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from schedule.models import TextForNewsletter


class TextForNewsletterListView(LoginRequiredMixin, ListView):
    model = TextForNewsletter


class TextForNewsletterCreateView(LoginRequiredMixin, CreateView):
    model = TextForNewsletter
    fields = ('subject', 'text',)
    success_url = reverse_lazy("schedule:textfornewsletter_list")


class TextForNewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = TextForNewsletter
    fields = ('subject', 'text',)

    def get_success_url(self):
        return reverse("schedule:textfornewsletter_list")


class TextForNewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = TextForNewsletter

    def get_success_url(self):
        return reverse("schedule:textfornewsletter_list")
