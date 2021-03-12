from rest_framework import serializers

from study.api.models import Subscription, UserMembership, Membership


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['slug', 'membership_type', 'price']


class UserMembershipSerializer(serializers.ModelSerializer):
    membership = MembershipSerializer()

    class Meta:
        model = UserMembership
        fields = ['user', 'membership']

    def create(self, validated_data):
        membership_data = validated_data.pop('membership')
        user_membership = UserMembership.objects.create(**validated_data)
        Membership.objects.create(user_membership=user_membership, **membership_data)
        return user_membership


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user_membership', 'active']

    def create(self, validated_data):
        user_membership_data = validated_data.pop('user_membership')
        subscription = Subscription.objects.create(**validated_data)
        UserMembership.objects.create(subscription=subscription, **user_membership_data)
        return subscription
