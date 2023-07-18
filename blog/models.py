from django.db import models
from uuslug import uuslug
from setup.base_model import SlugBaseModel


class Post(SlugBaseModel):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title

    def save(self):
        self.slug = uuslug(self.title, instance=self)
        return super().save()

    class Meta:
        ordering = ["-id"]
