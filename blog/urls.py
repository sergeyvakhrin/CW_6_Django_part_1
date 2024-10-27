from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/<int:pk>/view/', BlogDetailView.as_view(), name='blog_detail'),
]
