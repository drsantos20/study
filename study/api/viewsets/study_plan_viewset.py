from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from study.api.models.study_plan import StudyPlan
from study.api.permissions.user_membership_type_permission import IsPremiumAccount

from study.api.serializers.study_plan_serializer import (
    StudyPlanSerializer,
    StudyPlanAggregatedDataSerializer,
)


class StudyPlanViewSet(ModelViewSet):
    serializer_class = StudyPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyPlan.objects.filter(user_membership__user=self.request.user)

    @action(methods=['get'], detail=True, permission_classes=(IsPremiumAccount,), serializer_class=StudyPlanAggregatedDataSerializer)
    def get_lesson_aggregated_data(self, request, version, pk=None):
        study_plan = StudyPlan.objects.get(user_membership__user=self.request.user)
        serializer = self.get_serializer(study_plan, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
