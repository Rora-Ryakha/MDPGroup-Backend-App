from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from users.check import inn_check, login_check
from django.db import models


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:

        if view.action == "create":
            return inn_check(request) and login_check(request)
        else:
            return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["update", "partial_update"]:
            return obj == request.user
        elif view.action in ["retrieve", "list"]:
            return True
        elif view.action == "destroy":
            return request.user.is_staff or (obj == request.user) or (obj.owner == request.user)
        else:
            return False


class Images(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:

        if not request.user.is_authenticated:
            return False

        if view.action in ["update", "partial_update"]:
            return obj.owner == request.user
        elif view.action in ["retrieve", "list"]:
            return True
        elif view.action == "destroy":
            return request.user.is_staff or (obj.owner == request.user)
        else:
            return False
