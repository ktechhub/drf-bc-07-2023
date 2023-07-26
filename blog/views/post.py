import json
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from blog.models.comment import Comment
from blog.models.post import Post
from blog.serializers.post import PostSerializer, GeneralPostSerializer
from blog.serializers.comment import GeneralCommentSerializer
from blog.permissions import IsPostUserOnly


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsPostUserOnly]
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = "slug"
    queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all().filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return GeneralPostSerializer
        if self.action == "retrieve":
            return GeneralPostSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data["comments"] = GeneralCommentSerializer(
            Comment.objects.all().filter(post=instance), many=True
        ).data
        return Response(data)
