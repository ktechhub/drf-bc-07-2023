from rest_framework import serializers
from blog.models.post import Post
from users.serializers.user import UserDetailSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "image", "content"]


class GeneralPostSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Post
        fields = "__all__"
