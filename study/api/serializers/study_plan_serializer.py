from rest_framework import serializers

from study.api.models.study_plan import StudyPlan


class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['user_membership', 'reminder_date']
