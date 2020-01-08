from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pud_date <= now
    def has_choice_set(self):
        return (self.choice_set.all())>0

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
