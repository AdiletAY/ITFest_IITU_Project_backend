from django.urls import path
from apps.authentication.views import UserLoginAPI


urlpatterns = [
    path('login/', UserLoginAPI.as_view(), name="user_login"),
]
