from django.db import models

from study.api.models import UserMembership


class StudyPlan(models.Model):

    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    reminder_date = models.DateField(null=True, blank=True)
