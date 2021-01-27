from rest_framework import serializers

from study.api.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['topic', 'reminder_date']
