from unittest import TestCase

from study.api.factories import OrderFactory, MembershipFactory, UserMembershipFactory, SubscriptionFactory, UserFactory
from study.api.models.order import Order, SUCCESS
from study.api.models.membership import PREMIUM, FREE, UserMembership
from study.api.tasks import update_user_membership, request_order_payment


class TestOrder(TestCase):
    def setUp(self) -> None:
        self.membership = MembershipFactory(price=10.00)
        self.order = OrderFactory(membership=self.membership)

        self.user = UserFactory(first_name='John Due')
        self.user_membership = UserMembershipFactory(user=self.user)

    def test_order_model(self):
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(self.order.order_status, order.order_status)

        # Always pending
        self.assertEqual(order.total_price, 10.00)
        self.assertEqual(order.order_status, 'Pending')

    def test_update_user_membership_when_payment_processed_successfully(self):
        OrderFactory(user=self.user)

        user_membership = UserMembership.objects.get(id=self.user_membership.id)

        self.assertEqual(user_membership.membership.membership_type, FREE)
        update_user_membership(user_id=self.user.id)
        user_membership.refresh_from_db()
        self.assertEqual(user_membership.membership.membership_type, PREMIUM)

    def test_it_updates_order_with_pending_status_given_a_payment_processed_successfully(self):
        order = OrderFactory(user=self.user)
        request_order_payment(order_id=order.id)
        order.refresh_from_db()
        self.assertEqual(order.order_status, SUCCESS)

