from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import UserSerializer

from apps.users.serializers import UserLoginSerializer
from apps.authentication.services import (
    generate_tokens_for_user,
)


class UserLoginAPI(APIView):
    @extend_schema(request=UserLoginSerializer, responses=UserSerializer)
    def post(self, request, format=True):
        print('here')
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        serializer = UserSerializer(user)
        token = generate_tokens_for_user(user)

        return Response(
            status=status.HTTP_200_OK,
            data={
                "user": serializer.data,
                "token": token,
            },
        )
