from django.contrib.auth.models import User
from django.db import models


class StudyPlan(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reminder_date = models.DateField(null=True, blank=True)
