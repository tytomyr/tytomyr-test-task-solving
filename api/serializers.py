from rest_framework import serializers
from api.models import Post, Comment, Like
from user.models import Follower


class FollowerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "image",
        )


class FollowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "image"
        )
        read_only_fields = (
            "email",
            "first_name",
            "last_name",
            "image"
        )


class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "id",
            "post",
            "value",
            "user")


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "value",
            "user")


class PostListSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id",
                  "content",
                  "likes_count",
                  "followers",
                  "comments")

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_followers(self, obj):
        return obj.followed_by.count()

    def get_comments(self, obj):
        return obj.comments.count()


class PostDetailSerializer(serializers.ModelSerializer):
    likes = LikeListSerializer(many=True, read_only=False)
    comments = CommentListSerializer(many=True, read_only=False)
    posted_by = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="email"
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "posted_by",
            "content",
            "comments",
            "likes",
            "followed_by"
        )
