from rest_framework import serializers

from study.api.models.study_plan import StudyPlan
from study.api.serializers.lesson_serializer import LessonSerializer


class StudyPlanSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(required=False, many=True)

    class Meta:
        model = StudyPlan
        fields = ['id', 'user_membership', 'reminder_date', 'lessons']


class StudyPlanAggregatedDataSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'total_lessons_count': instance.lessons.count(),
        }
