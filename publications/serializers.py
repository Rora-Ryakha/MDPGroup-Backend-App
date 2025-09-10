from rest_framework import serializers

from .models import (Card, CardComment, CardImage, CardFile,
                     CardCommentImage)


class CardImageSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = CardImage
        fields = "__all__"


class CardFileSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = CardFile
        fields = "__all__"


class CardCommentImageSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = CardCommentImage
        fields = "__all__"


class CardCommentSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = CardComment
        fields = ["owner", "card", "text", "rating", "time_published", "time_updated", "images"]


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Card
        fields = ["owner", "card_name", "caption", "tags", "price", "num_of_views", "num_of_resp", "rating",
                  "time_published", "time_updated", "images", "files", "comments", "categories"]
