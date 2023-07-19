from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models.custom_user import CustomUser
from users.models.verification_code import VerificationCode


admin.site.site_header = "Django BootCamp C-Panel"
admin.site.site_title = "Django BootCamp C-Panel"


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "username",
        "is_admin",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "username",
        "is_admin",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "email",
        "username",
    )
    ordering = (
        "is_staff",
        "email",
        "username",
    )
    readonly_fields = ("date_joined", "last_login")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(VerificationCode)
