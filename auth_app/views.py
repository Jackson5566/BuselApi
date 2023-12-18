from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import GetUserSerializer, CreateUserSerializer
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import status
from rest_framework.generics import CreateAPIView


class UsersView(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def authenticated_user(request) -> Response:
    user_serializer = GetUserSerializer(instance=request.user)
    return Response(user_serializer.data, status=status.HTTP_200_OK)
