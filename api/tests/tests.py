from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from api import serializers, models
from user.models import Follower, User


class FollowerModelTestCase(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            email="test1@example.com", password="password"
        )
        self.user2 = get_user_model().objects.create_user(
            email="test2@example.com", password="password"
        )
        self.follower = Follower.objects.create(
            user=self.user1,
            username="testuser",
            first_name="John",
            last_name="Doe",
            bio="Test bio",
        )

    def test_followed_by_relation(self):
        self.follower.followed_by.add(self.user2)
        self.assertIn(self.user2, self.follower.followed_by.all())


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.post = models.Post.objects.create(
            content="Test content", posted_by=self.user
        )

    def test_post_str_method(self):
        self.assertEqual(str(self.post), "Test content")


class LikeModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.post = models.Post.objects.create(
            content="Test content", posted_by=self.user
        )
        self.like = models.Like.objects.create(
            value=models.Like.LikeChoice.LIKE, post=self.post, user=self.user
        )

    def test_like_str_method(self):
        self.assertEqual(str(self.like), "👍")

    def test_like_uniqueness_constraint(self):
        with self.assertRaises(Exception):
            models.Like.objects.create(
                value=models.Like.LikeChoice.LIKE, post=self.post, user=self.user
            )


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )
        self.post = models.Post.objects.create(
            content="Test content", posted_by=self.user
        )
        self.comment = models.Comment.objects.create(
            value="Test comment", post=self.post, user=self.user
        )

    def test_comment_uniqueness_constraint(self):
        with self.assertRaises(Exception):
            models.Comment.objects.create(
                value="Test comment", post=self.post, user=self.user
            )
