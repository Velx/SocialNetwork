from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer, UserActivitySerializer,\
    CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    @action(detail=True, methods=['GET'])
    def activity(self, request, username=None):
        user = self.get_object()
        serializer = UserActivitySerializer(user)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
