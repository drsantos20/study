from unittest.mock import MagicMock, patch

from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status


class TestUserViewSet(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = MagicMock(username='batman', email='batman@dc.com', password='kjdhabida7yi84')

    def test_create_user(self):
        data = {
            'username': self.user.username,
            'email': self.user.email,
            'password': self.user.password
        }

        url = '/api/v1/account/register'
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @patch('study.api.tasks.create_user_membership')
    def test_create_membership_when_user_is_created(self, create_membership):
        user = User.objects.create(
            username='drsantos20',
            email='drsantos20@gmail.com',
            password='q1w2e3',
        )
        create_membership(user.id)
        create_membership.assert_called_with(1)
