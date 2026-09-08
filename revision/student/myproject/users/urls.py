from django.urls import path

from .views import user_api


urlpatterns = [
    path(
        "users/",
        user_api,
        name="user_api"
    ),
]