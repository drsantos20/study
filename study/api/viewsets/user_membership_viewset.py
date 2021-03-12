from rest_framework.viewsets import ReadOnlyModelViewSet

from study.api.models import UserMembership, Subscription
from study.api.serializers.membership_serializer import UserMembershipSerializer, SubscriptionSerializer


class UserMembershipViewSet(ReadOnlyModelViewSet):
    serializer_class = UserMembershipSerializer

    def get_queryset(self):
        return UserMembership.objects.filter(user__id=self.kwargs['pk']).select_related('user')


class SubscriptionViewSet(ReadOnlyModelViewSet):
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user_membership__user__id=self.kwargs['pk']).select_related('user_membership__user')
