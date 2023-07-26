from django.db import models
from django.contrib.auth import get_user_model
from uuslug import uuslug
from blog.directories import post_directory
from setup.base_model import SlugBaseModel

User = get_user_model()


class Post(SlugBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=post_directory)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-id"]
