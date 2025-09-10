from django.db import models
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from users.models import CustomUser
from .models import Card, CardComment


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["update", "partial_update"]:
            return obj.owner == request.user
        elif view.action == "retrieve":
            return True
        elif view.action == "destroy":
            return request.user.is_staff or (obj.owner == request.user)
        else:
            return False


class CardFilesImages(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        if view.action == "create":
            return (CustomUser.objects.filter(login=request.user).values()[0]["id"] ==
                    Card.objects.filter(id=request.data["card"]).values()[0]["owner_id"])
        return request.user.is_authenticated

    def has_object_permission(
            self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["update", "partial_update"]:
            return obj.owner == request.user
        elif view.action == "retrieve":
            return True
        elif view.action == "destroy":
            return request.user.is_staff or (obj.owner == request.user)
        else:
            return False


class CommentFilesImages(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        if view.action == "create":
            return (CustomUser.objects.filter(login=request.user).values()[0]["id"] ==
                    CardComment.objects.filter(id=request.data["comment"]).values()[0]["owner_id"])
        return request.user.is_authenticated

    def has_object_permission(
            self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["update", "partial_update"]:
            return obj.owner == request.user
        elif view.action == "retrieve":
            return True
        elif view.action == "destroy":
            return request.user.is_staff or (obj.owner == request.user)
        else:
            return False
