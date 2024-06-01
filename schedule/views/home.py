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

        context["newsletters_done_count"] = newsletters_done_count
        context["newsletters_active"] = newsletters_active

        blog = Blog.objects.all()
        blog_pk = blog.values_list("pk", flat=True)
        blog_pk_list = list(blog_pk)
        shuffle(blog_pk_list)
        blogs_list = list()
        for pk in blog_pk_list[:3]:
            blogs_list.append(blog.get(pk=pk))

        context["blogs_list"] = blogs_list

        return context
