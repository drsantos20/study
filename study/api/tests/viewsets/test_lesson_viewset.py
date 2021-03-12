import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import LessonFactory
from study.api.models import Lesson


class TestLessonViewSet(APITestCase):
    def setUp(self) -> None:
        self.lesson = LessonFactory()
        self.client = APIClient()

    def test_list_lessons(self):
        response = self.client.get(
            reverse('lesson-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_lesson(self):
        data = json.dumps({
            'topic': 'Python Variables Topic',
        })
        response = self.client.post(
            reverse('lesson-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lesson(self):
        response = self.client.get(
            reverse('lesson-detail', kwargs={'version': 'v1', 'pk': self.lesson.id}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        lesson_data = json.loads(response.content)
        self.assertEqual(lesson_data['topic'], self.lesson.topic)

    def test_update_lesson(self):
        data = json.dumps({
            'topic': 'Update Python Variables Topic',
        })

        response = self.client.put(
            reverse('lesson-detail', kwargs={'version': 'v1', 'pk': self.lesson.id}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        lesson = Lesson.objects.get(id=self.lesson.id)
        self.assertEqual(lesson.topic, 'Update Python Variables Topic')

    def test_delete_lesson(self):
        response = self.client.delete(
            reverse('lesson-detail', kwargs={'version': 'v1', 'pk': self.lesson.id}),
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        lesson = Lesson.objects.filter(id=self.lesson.id)
        self.assertFalse(lesson.exists())
