from django.test import TestCase

from study.api.factories import OrderFactory, MembershipFactory
from study.api.serializers.order_serializer import OrderCreateSerializer, OrderReadSerializer


class TestOrderCreateSerializer(TestCase):

    def setUp(self):
        self.membership = MembershipFactory(price=10.00)
        self.order = OrderFactory(membership=self.membership)
        self.order_serializer = OrderCreateSerializer(instance=self.order)

    def test_order_create_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data['order_status'], self.order.order_status)
        self.assertEqual(serializer_data['order_status'], 'Pending')


class TestOrderReadSerializer(TestCase):

    def setUp(self):
        self.membership = MembershipFactory(price=10.00)
        self.order = OrderFactory(membership=self.membership)
        self.order_serializer = OrderReadSerializer(instance=self.order)

    def test_order_read_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(serializer_data['order_status'], self.order.order_status)
        self.assertEqual(serializer_data['order_status'], 'Pending')
        self.assertEqual(serializer_data['total_price'], self.order.total_price)
