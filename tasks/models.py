from django.db import models
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255, default='')
    is_finished = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    reopened = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title