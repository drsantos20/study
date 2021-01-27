from unittest import TestCase

from study.api.factories import LessonFactory
from study.api.models import Lesson


class TestLesson(TestCase):
    def setUp(self) -> None:
        self.lesson = LessonFactory()

    def test_lesson_model(self):
        lesson = Lesson.objects.get(id=self.lesson.id)
        self.assertEqual(self.lesson.topic, lesson.topic)
