from django.test import TestCase

from study.api.factories import LessonFactory
from study.api.serializers.lesson_serializer import LessonSerializer


class TestLessonSerializer(TestCase):

    def setUp(self):
        self.lesson = LessonFactory()
        self.lesson_serializer = LessonSerializer(instance=self.lesson)

    def test_lesson_serializer(self):
        serializer_data = self.lesson_serializer.data
        self.assertEqual(serializer_data['topic'], self.lesson.topic)
