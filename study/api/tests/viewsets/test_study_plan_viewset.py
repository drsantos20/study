import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import LessonFactory, UserFactory, UserMembershipFactory, StudyPlanFactory, MembershipFactory
from study.api.models.membership import PREMIUM
from study.api.tests.utils import create_token, get_token_from_user


class TestStudyPlanViewSet(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = UserFactory(first_name='John Due')
        self.membership = MembershipFactory(membership_type=PREMIUM)
        self.user_membership = UserMembershipFactory(user=self.user, membership=self.membership)
        self.lesson = LessonFactory()
        self.study_plan = StudyPlanFactory(user_membership=self.user_membership, lessons=[self.lesson])
        create_token(user=self.user)

    def test_list_study_plan_from_user(self):
        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('study-plan-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        study_plan_data = json.loads(response.content)[0]
        self.assertEqual(study_plan_data['id'], self.study_plan.id)
        self.assertEqual(study_plan_data['lessons'][0]['topic'], self.study_plan.lessons.all()[0].topic)

    def test_study_plan_aggregated_data_feature_for_premium_accounts(self):
        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('study-plan-get-lesson-aggregated-data', kwargs={'version': 'v1', 'pk': self.study_plan.id}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        study_plan_data = json.loads(response.content)
        self.assertEqual(study_plan_data['total_lessons_count'], 1)

    def test_it_returns_403_for_free_user_when_access_study_plan_aggregated_data_feature_for_premium_accounts(self):
        user = UserFactory(first_name='Spike Lee')
        user_membership = UserMembershipFactory(user=user)
        lesson = LessonFactory()
        study_plan = StudyPlanFactory(user_membership=user_membership, lessons=[lesson])
        create_token(user=user)

        token = get_token_from_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('study-plan-get-lesson-aggregated-data', kwargs={'version': 'v1', 'pk': study_plan.id}),
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

