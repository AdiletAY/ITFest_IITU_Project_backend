from django.urls import path
from apps.users.views import UserRetrieveAPI
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('me/', UserRetrieveAPI.as_view(), name="auth_me"),
]
