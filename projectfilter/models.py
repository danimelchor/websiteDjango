from django.db import models
from django.utils import timezone, formats
from django.contrib.auth.models import User
from django.template.defaultfilters import date



class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_img = models.CharField(max_length=100)
    project_tags = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name
