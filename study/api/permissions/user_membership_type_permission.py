from rest_framework.permissions import BasePermission

from study.api.models import UserMembership
from study.api.models.membership import PREMIUM


class IsPremiumAccount(BasePermission):

    def has_permission(self, request, view):
        user_membership = UserMembership.objects.get(user=request.user)
        membership = user_membership.membership
        return membership.membership_type == PREMIUM
