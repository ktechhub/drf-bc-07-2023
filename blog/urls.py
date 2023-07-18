from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet


router = DefaultRouter()

router.register("api/posts", PostsViewSet)

urlpatterns = [path("", include(router.urls))]
