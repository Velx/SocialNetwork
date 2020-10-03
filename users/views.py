from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

