from django.db import models


class Questionnaire(models.Model):
    user = models.EmailField()
    occupation = models.TextField()
    discovery = models.TextField()
    usageExplanation = models.TextField()
