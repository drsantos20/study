import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import LessonFactory, UserFactory, UserMembershipFactory, StudyPlanFactory
from study.api.tests.utils import create_token, get_token_from_user


class TestLessonViewSet(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = UserFactory(first_name='John Due')
        self.user_membership = UserMembershipFactory(user=self.user)
        self.lesson = LessonFactory()
        self.study_plan = StudyPlanFactory(user_membership=self.user_membership, lessons=[self.lesson])
        create_token(user=self.user)

    def test_list_lessons_given_a_study_plan(self):
        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('lesson-detail', kwargs={'version': 'v1', 'pk': self.study_plan.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['topic'], self.lesson.topic)

    def test_add_lesson_to_user_study_plan(self):
        lesson = LessonFactory()
        data = json.dumps({
            'topic': lesson.topic
        })

        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.post(
            reverse('lesson-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
