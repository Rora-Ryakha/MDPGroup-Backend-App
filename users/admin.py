from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
        "username",
        "inn",
        "login",
        "logo",
        "caption",
        "contacts",
        "tags",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "username",
        "inn",
        "login",
        "logo",
        "caption",
        "contacts",
        "tags",
        "rating",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": (
            "username",
            "inn",
            "login",
            "password",
            "logo",
            "caption",
            "contacts",
            "tags",
        )}
         ),
        ("Permissions", {"fields": (
            "is_staff",
            "is_active",
            "groups",
            "user_permissions")}
         ),
    )
    add_fieldsets = (
        (None, {"fields": (
            "username",
            "inn",
            "login",
            "password1",
            "password2",
            "logo",
            "caption",
            "contacts",
            "tags",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions")}
         ),
    )
    search_fields = ("username", "inn")
    ordering = ("username", )


admin.site.register(CustomUser, CustomUserAdmin)
