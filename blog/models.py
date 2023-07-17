from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-id"]
