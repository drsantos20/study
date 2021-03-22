from django.db import models


class StudyPlan(models.Model):

    name = models.CharField(max_length=35, null=True)
    user_membership = models.ForeignKey('UserMembership', on_delete=models.CASCADE, null=True)
    reminder_date = models.DateField(null=True, blank=True)
    lessons = models.ManyToManyField('Lesson', related_name='study_plans', null=True)
