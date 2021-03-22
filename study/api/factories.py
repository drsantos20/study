import factory
from django.contrib.auth.models import User

from study.api.models import Lesson, Membership, UserMembership, Subscription
from study.api.models.order import Order
from study.api.models.study_plan import StudyPlan


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


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


class OrderFactory(factory.django.DjangoModelFactory):
    membership = factory.SubFactory(MembershipFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order


class LessonFactory(factory.django.DjangoModelFactory):
    topic = factory.Faker('pystr')

    class Meta:
        model = Lesson


class StudyPlanFactory(factory.django.DjangoModelFactory):
    user_membership = factory.SubFactory(UserMembershipFactory)
    reminder_date = factory.Faker('date_object')
    name = factory.Faker('pystr')

    class Meta:
        model = StudyPlan

    @factory.post_generation
    def lessons(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for lesson in extracted:
                self.lessons.add(lesson)
