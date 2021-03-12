from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from study.api.serializers.user_serializer import UserSerializer


class UserCreateViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
