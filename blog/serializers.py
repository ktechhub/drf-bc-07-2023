from rest_framework import serializers
from blog.models.post import Post
from blog.models.comment import Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ['title', 'content']
