from django.db import models
from test_api import settings


class Post(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followed_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="followed"
    )

    def __str__(self):
        return self.content


class Like(models.Model):
    class LikeChoice(models.TextChoices):
        LIKE = "👍"
        DISLIKE = "👎"

    value = models.CharField(max_length=50, choices=LikeChoice.choices)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )

    def __str__(self):
        return self.value

    class Meta:
        unique_together = ["value", "post", "user"]


class Comment(models.Model):
    value = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        unique_together = ["value", "post", "user"]
