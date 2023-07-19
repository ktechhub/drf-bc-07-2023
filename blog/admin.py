from django.contrib import admin

from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "is_active",
        "views",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["slug"]


admin.site.register(Post, PostAdmin)
