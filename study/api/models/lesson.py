from django.contrib.auth.models import User
from django.db import models


class Lesson(models.Model):

    topic = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reminder_date = models.DateField(null=True, blank=True)
