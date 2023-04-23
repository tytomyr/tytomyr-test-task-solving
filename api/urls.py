from django.urls import path, include
from rest_framework import routers
from api.views import (PostViewSet,
                       CommentViewSet,
                       LikeViewSet)


router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet),
router.register("likes", LikeViewSet),

urlpatterns = [
    path("", include(router.urls))
]

app_name = "api"
