from unittest import TestCase

from study.api.factories import OrderFactory, MembershipFactory, UserMembershipFactory, SubscriptionFactory
from study.api.models.order import Order


class TestOrder(TestCase):
    def setUp(self) -> None:
        self.membership = MembershipFactory(price=10.00)
        self.order = OrderFactory(membership=self.membership)

    def test_order_model(self):
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(self.order.order_status, order.order_status)

        # Always pending
        self.assertEqual(order.total_price, 10.00)
        self.assertEqual(order.order_status, 'Pending')
