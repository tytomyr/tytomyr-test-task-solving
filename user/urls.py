from django.urls import path, include
from user.views import (CreateUserView,
                        CreateTokenView,
                        ManageUserView,
                        FollowerViewSet)

from rest_framework import routers


router = routers.SimpleRouter()
router.register("users", FollowerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
