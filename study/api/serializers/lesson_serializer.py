from rest_framework import serializers

from study.api.models import Lesson, UserMembership
from study.api.models.study_plan import StudyPlan


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['topic']

    @property
    def get_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        lesson_data = validated_data.pop('topic')
        lesson = Lesson.objects.create(topic=lesson_data)

        user_membership = UserMembership.objects.get(user=self.get_user)
        study_plan = StudyPlan.objects.get(user_membership=user_membership)
        study_plan.lessons.add(lesson)
        study_plan.save()
        return lesson
