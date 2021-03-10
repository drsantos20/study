import datetime

import factory
from django.contrib.auth.models import User

from study.api.models import Lesson


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class LessonFactory(factory.django.DjangoModelFactory):
    topic = factory.Faker('pystr')

    class Meta:
        model = Lesson

