from rest_framework.viewsets import ModelViewSet

from study.api.models import Lesson
from study.api.serializers.lesson_serializer import LessonSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
