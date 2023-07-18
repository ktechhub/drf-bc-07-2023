import json
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer


class PostsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
