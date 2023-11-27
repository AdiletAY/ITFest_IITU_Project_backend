from rest_framework import serializers
from apps.users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "user_permissions",
            "last_login",
            "groups",
        ]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
