from django.test import TestCase


from study.api.factories import (
    MembershipFactory,
    UserMembershipFactory,
    SubscriptionFactory,
)

from study.api.serializers.membership_serializer import (
    MembershipSerializer,
    UserMembershipSerializer,
    SubscriptionSerializer,
)


class TestMembershipSerializer(TestCase):

    def setUp(self):
        self.membership = MembershipFactory()

    def test_it_serializes_all_fields_when_provided_a_membership(self):
        serializer = MembershipSerializer(instance=self.membership)
        self.assertEqual(serializer.data['slug'], self.membership.slug)
        self.assertEqual(serializer.data['membership_type'], self.membership.membership_type)


class TestUserMembershipSerializer(TestCase):

    def setUp(self):
        self.user_membership = UserMembershipFactory()

    def test_it_serializes_all_fields_when_provided_a_user_membership(self):
        serializer = UserMembershipSerializer(instance=self.user_membership)
        self.assertEqual(serializer.data['user'], self.user_membership.user.id)
        self.assertEqual(serializer.data['membership']['membership_type'], self.user_membership.membership.membership_type)
        self.assertEqual(serializer.data['membership']['slug'], self.user_membership.membership.slug)


class TestSubscriptionSerializer(TestCase):

    def setUp(self):
        self.subscription = SubscriptionFactory()

    def test_it_serializes_all_fields_when_provided_a_subscription(self):
        serializer = SubscriptionSerializer(instance=self.subscription)
        self.assertEqual(serializer.data['active'], self.subscription.active)
        self.assertEqual(serializer.data['user_membership'], self.subscription.user_membership_id)
