from unittest.mock import MagicMock

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
