from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views.post import PostsViewSet


router = DefaultRouter()

router.register("posts", PostsViewSet)

urlpatterns = [path("", include(router.urls))]
