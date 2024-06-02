from random import shuffle

from django.views.generic import ListView

from blog.models import Blog
from schedule.models import Newsletter, DONE, STARTED


class HomeView(ListView):
    model = Newsletter
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()
        newsletters = queryset.filter()

        newsletters_done_count = newsletters.filter(status_of_newsletter=DONE).count()
        newsletters_active = newsletters.filter(status_of_newsletter=STARTED).count()
        unique_clients = (
            newsletters.prefetch_related("clients").all().distinct().count()
        )

        context["newsletters_done_count"] = newsletters_done_count
        context["newsletters_active"] = newsletters_active
        context["unique_clients"] = unique_clients

        blog_pks = list(Blog.objects.values_list("pk", flat=True))
        shuffle(blog_pks)
        selected_blog_pks = blog_pks[:3]
        blogs_list = Blog.objects.filter(pk__in=selected_blog_pks)

        context["blogs_list"] = blogs_list

        return context
