import datetime

import factory
from django.contrib.auth.models import User

from study.api.models import Lesson, Membership, UserMembership, Subscription


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class LessonFactory(factory.django.DjangoModelFactory):
    topic = factory.Faker('pystr')

    class Meta:
        model = Lesson


class MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership


class UserMembershipFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    membership = factory.SubFactory(MembershipFactory)

    class Meta:
        model = UserMembership


class SubscriptionFactory(factory.django.DjangoModelFactory):
    user_membership = factory.SubFactory(UserMembershipFactory)
    active = factory.Faker('pybool')

    class Meta:
        model = Subscription
