from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "inn",
            "login",
            "password",
            "logo",
            "caption",
            "contacts",
            "tags",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions"
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "inn",
            "login",
            "password",
            "logo",
            "caption",
            "contacts",
            "tags",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions"
        ]
