from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import LessonFactory


class TestLessonViewSet(APITestCase):
    def setUp(self) -> None:
        self.lesson = LessonFactory()
        self.client = APIClient()

    def test_list_lessons(self):
        response = self.client.get(
            reverse('lesson-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
