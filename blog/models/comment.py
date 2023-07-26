from django.db import models
from django.contrib.auth import get_user_model
from setup.base_model import BaseModel
from .post import Post


User = get_user_model()


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} - {self.post.title}"

    class Meta:
        ordering = ["-id"]
