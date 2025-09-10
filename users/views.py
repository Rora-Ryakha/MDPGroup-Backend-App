from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import (CustomUser, UserImage)
from .serializers import (UserSerializer, UserImageSerializer)
from .permissions import IsOwnerOrReadOnly, Images


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserImageViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = (Images,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
