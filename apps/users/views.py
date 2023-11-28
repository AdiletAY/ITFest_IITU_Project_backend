from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import UserSerializer
from apps.authentication.services import generate_tokens_for_user
# Create your views here.


class UserRetrieveAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = request.user
        token = generate_tokens_for_user(user)
        serializer = self.serializer_class(user)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "user": serializer.data,
                "token": token
            }
        )
