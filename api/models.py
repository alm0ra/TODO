from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Task's Title")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="created date", blank=True)
    status = models.BooleanField(default=False, blank=True, null=True, verbose_name="Task's Status")

    class Meta :
        verbose_name = "Tasks"
        verbose_name_plural= "Tasks"
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title