import json
from unittest.mock import patch

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from study.api.factories import OrderFactory, UserFactory, UserMembershipFactory
from study.api.models import Order
from study.api.tests.utils import get_token_from_user, create_token


class TestOrderViewSet(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory(first_name='John Due')
        self.user_membership = UserMembershipFactory(user=self.user)
        self.client = APIClient()
        create_token(user=self.user)

    def test_list_orders_from_user(self):
        OrderFactory(user=self.user)

        token = get_token_from_user(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order = Order.objects.get(user=self.user)
        self.assertEqual(order.order_status, 'Pending')

    def test_get_order_detail(self):
        order = OrderFactory(user=self.user)
        token = get_token_from_user(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('order-get-order-detail', kwargs={'version': 'v1', 'pk': order.id}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)
        self.assertEqual(order_data['order_status'], order.order_status)

    def test_it_returns_404_for_a_user_trying_to_access_a_order_from_another_user(self):
        new_user = UserFactory()
        create_token(user=new_user)
        order = OrderFactory(user=self.user)

        token = get_token_from_user(user=new_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.get(
            reverse('order-get-order-detail', kwargs={'version': 'v1', 'pk': order.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('study.api.tasks.request_order_payment')
    def test_create_payment_request(self, payment_order_request):
        order = OrderFactory()
        payment_order_request(order.id)
        payment_order_request.assert_called_with(1)

