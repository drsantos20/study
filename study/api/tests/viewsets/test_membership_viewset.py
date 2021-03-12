import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import UserMembershipFactory, SubscriptionFactory


class TestUserMembershipViewSet(APITestCase):
    def setUp(self) -> None:
        self.user_membership = UserMembershipFactory()
        self.client = APIClient()

    def test_get_user_membership(self):
        response = self.client.get(
            reverse('user-membership-detail', kwargs={'version': 'v1', 'pk': self.user_membership.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)

        self.assertEqual(response_data['membership']['slug'], self.user_membership.membership.slug)
        self.assertEqual(response_data['membership']['membership_type'], self.user_membership.membership.membership_type)
        self.assertEqual(response_data['user'], self.user_membership.user.id)


class TestSubscriptionViewSet(APITestCase):
    def setUp(self) -> None:
        self.subscription = SubscriptionFactory(active=True)
        self.client = APIClient()

    def test_get_user_subscription(self):
        response = self.client.get(
            reverse('subscription-detail', kwargs={'version': 'v1', 'pk': self.subscription.user_membership.user.id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)

        self.assertTrue(response_data['active'])
        self.assertEqual(response_data['active'], self.subscription.active)
        self.assertEqual(response_data['user_membership'], self.subscription.user_membership.user.id)
