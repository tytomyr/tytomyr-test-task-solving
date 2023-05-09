from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import Follower


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "email",
            "password",
            "is_staff",
        )
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class FollowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "image",
        )


class FollowerDetailSerializer(FollowerListSerializer):
    followers = UserListSerializer(many=True, read_only=True)

    class Meta(FollowerListSerializer.Meta):
        fields = FollowerListSerializer.Meta.fields + ("followers",)
