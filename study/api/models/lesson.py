from django.db import models


class Lesson(models.Model):

    topic = models.CharField(max_length=100)
