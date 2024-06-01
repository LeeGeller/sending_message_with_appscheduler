from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog


class DispatchMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return PermissionDenied("Go out!")
        else:
            return super().dispatch(request, *args, **kwargs)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")


class BlogCreateView(LoginRequiredMixin, DispatchMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        user = self.request.user
        blog = form.save(commit=False)
        blog.author = user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, DispatchMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("blog:blog_list")

    def form_valid(self, form):
        user = self.request.user
        blog = form.save(commit=False)
        blog.author = user
        return super().form_valid(form)
