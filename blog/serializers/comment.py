from rest_framework import serializers
from blog.models.comment import Comment
from users.serializers.user import UserDetailSerializer
from .post import GeneralPostSerializer


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugField()

    class Meta:
        model = Comment
        fields = ["post", "content"]


class GeneralCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    post = GeneralPostSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
