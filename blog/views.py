import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from blog.serializers import PostSerializer


@api_view(["GET"])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
