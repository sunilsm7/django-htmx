from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
