from django.db import models


class BaseModel(models.Model):
    views = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def increase_views(self):
        self.views += 1
        self.save()

    class Meta:
        abstract = True


class SlugBaseModel(BaseModel):
    slug = models.SlugField(max_length=256, unique=True, editable=False)

    class Meta:
        abstract = True
