from django.test import TestCase

from study.api.factories import MembershipFactory, UserMembershipFactory, SubscriptionFactory
from study.api.models import Membership, UserMembership, Subscription


class MembershipTestCase(TestCase):
    def setUp(self) -> None:
        self.membership = MembershipFactory()

    def test_get_membership(self):
        membership = Membership.objects.get(id=self.membership.id)
        self.assertEqual(membership.slug, self.membership.slug)
        self.assertEqual(membership.membership_type, self.membership.membership_type)
        self.assertEqual(membership.price, self.membership.price)


class UserMembershipTestCase(TestCase):
    def setUp(self) -> None:
        self.user_membership = UserMembershipFactory()

    def test_get_membership(self):
        user_membership = UserMembership.objects.get(id=self.user_membership.id)
        self.assertEqual(user_membership.membership.slug, self.user_membership.membership.slug)
        self.assertEqual(user_membership.membership.membership_type, self.user_membership.membership.membership_type)
        self.assertEqual(user_membership.membership.price, self.user_membership.membership.price)


class SubscriptionTestCase(TestCase):
    def setUp(self) -> None:
        self.subscription = SubscriptionFactory()

    def test_get_membership(self):
        subscription = Subscription.objects.get(id=self.subscription.id)
        self.assertEqual(subscription.active, self.subscription.active)
        self.assertEqual(subscription.user_membership.user.id, self.subscription.user_membership.user.id)
