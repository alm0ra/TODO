from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    models.DateTimeField(auto_now_add=True, verbose_name="created date")
    status = models.BooleanField(default=False, blank=True, null=True)

    class Meta :
        verbose_name = "Tasks"
        verbose_name_plural= "Tasks"
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title