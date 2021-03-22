from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from study.api.models import Order, Lesson
from study.api.serializers.lesson_serializer import LessonSerializer
from study.api.serializers.order_serializer import OrderCreateSerializer, OrderReadSerializer


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lesson.objects.filter(study_plans__id=self.kwargs['pk'])
