from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=False, max_length=255)
    login = models.CharField(max_length=255, unique=True)
    inn = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(null=True, blank=True)
    caption = models.TextField(blank=True)
    contacts = models.JSONField(null=True, blank=True)
    tags = models.JSONField()
    rating = models.FloatField(null=True, blank=True, editable=False)
    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = [
        "username",
        "inn"
    ]
    objects = CustomUserManager()


class UserImage(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="images")
    data = models.ImageField()
