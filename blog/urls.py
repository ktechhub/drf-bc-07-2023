from django.urls import path, include, re_path

from .views import get_posts

urlpatterns = [path("api/posts/", get_posts)]
