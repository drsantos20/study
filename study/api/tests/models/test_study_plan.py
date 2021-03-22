from unittest import TestCase

from study.api.factories import StudyPlanFactory, LessonFactory
from study.api.models.study_plan import StudyPlan


class TestStudyPlan(TestCase):
    def setUp(self) -> None:
        self.lesson = LessonFactory()
        self.study_plan = StudyPlanFactory(lessons=[self.lesson])

    def test_study_plan(self):
        study_plan = StudyPlan.objects.get(id=self.study_plan.id)
        self.assertEqual(self.study_plan.lessons.all()[0].topic, study_plan.lessons.all()[0].topic)
        self.assertEqual(self.study_plan.user_membership.user.id, study_plan.user_membership.user.id)
