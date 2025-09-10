import django_filters.rest_framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import (Card, CardComment, CardFile, CardImage,
                     CardCommentImage)
from .permissions import IsOwnerOrReadOnly, CardFilesImages, CommentFilesImages
from .serializers import (CardSerializer, CardCommentSerializer,
                          CardFileSerializer, CardImageSerializer,
                          CardCommentImageSerializer)
from users.models import CustomUser


# TODO: если поставил галку не показывать цену
class CardViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardCommentViewSet(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        new_rating = 0
        comment_count = 0
        for comment in CardComment.objects.all():
            new_rating += comment.rating
            comment_count += 1

        new_rating /= comment_count + 1
        card = Card.objects.filter(id=self.request.data["card"])
        card.update(rating=new_rating)
        # TODO: это какой-то костыль, разобраться
        CustomUser.objects.filter(id=card.values("owner_id")[0]["owner_id"]).update(rating=new_rating)


class CardImageViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    queryset = CardImage.objects.all()
    serializer_class = CardImageSerializer
    permission_classes = (CardFilesImages, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardFileViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = CardFile.objects.all()
    serializer_class = CardFileSerializer
    permission_classes = (CardFilesImages, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardCommentImageViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              GenericViewSet):
    queryset = CardCommentImage.objects.all()
    serializer_class = CardCommentImageSerializer
    permission_classes = (CommentFilesImages, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
