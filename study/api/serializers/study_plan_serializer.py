from rest_framework import serializers

from study.api.models import UserMembership, Lesson
from study.api.models.study_plan import StudyPlan
from study.api.serializers.lesson_serializer import LessonSerializer


class StudyPlanSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(required=False, many=True)

    class Meta:
        model = StudyPlan
        fields = ['id', 'user_membership', 'reminder_date', 'lessons', 'name']

    @property
    def get_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        lesson_data = validated_data.pop('lessons')
        user_membership = UserMembership.objects.get(user=self.get_user)
        study_plan = StudyPlan.objects.create(user_membership=user_membership, **validated_data)

        for lesson in lesson_data:
            lesson = Lesson.objects.create(topic=lesson['topic'])
            study_plan.lessons.add(lesson)
        study_plan.save()
        return study_plan


class StudyPlanAggregatedDataSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'total_lessons_count': instance.lessons.count(),
        }
