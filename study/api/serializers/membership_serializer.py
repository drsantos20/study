from rest_framework import serializers

from study.api.models.study_plan import StudyPlan


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['slug', 'membership_type', 'price']


class UserMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['user', 'membership']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = ['user_membership', 'active']
