from django.test import TestCase

from study.api.factories import StudyPlanFactory, LessonFactory
from study.api.serializers.study_plan_serializer import StudyPlanSerializer


class TestStudyPlanSerializer(TestCase):

    def setUp(self):
        self.lesson_1 = LessonFactory()
        self.lesson_2 = LessonFactory()
        self.study_plan = StudyPlanFactory(lessons=[self.lesson_1, self.lesson_2])
        self.study_plan_serializer = StudyPlanSerializer(instance=self.study_plan)

    def test_study_plan_serializer(self):
        serializer_data = self.study_plan_serializer.data
        self.assertEqual(serializer_data['user_membership'], self.study_plan.user_membership.id)
        self.assertEqual(serializer_data['lessons'][0]['topic'], self.study_plan.lessons.all()[0].topic)
        self.assertEqual(serializer_data['lessons'][1]['topic'], self.study_plan.lessons.all()[1].topic)

