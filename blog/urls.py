from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView

app_name = BlogConfig.name


urlpatterns = [
    path("blog-list/", BlogListView.as_view(), name="blog_list"),
    path("blog-form/", BlogCreateView.as_view(), name="blog_form"),
    path("<int:pk>/blog_update/", BlogUpdateView.as_view(), name="blog_update"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
