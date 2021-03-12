from unittest.mock import MagicMock

from django.contrib.auth.models import User
from django.test import TestCase

from study.api.serializers.user_serializer import UserSerializer


class TestUserSerializer(TestCase):

    def setUp(self):
        self.user = MagicMock(username='batman', email='batman@dc.com', password='kjdhabida7yi84')

    def test_it_creates_user(self):
        serializer_data = {
            'username': self.user.username,
            'email': self.user.email,
            'password': self.user.password
        }

        serializer = UserSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        created_user = User.objects.get(email='batman@dc.com')
        self.assertEqual(self.user.email, created_user.email)
        self.assertEqual(self.user.username, created_user.username)
