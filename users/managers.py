from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(
            self,
            login,
            password,
            username,
            **extra_fields
    ):
        if not login:
            raise ValueError(_("Придумайте логин"))
        if not username:
            raise ValueError(_("Придумайте имя пользователя"))
        user = self.model(
            username=username,
            login=login,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self,
            login,
            password,
            username,
            **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(login, password, username, **extra_fields)
