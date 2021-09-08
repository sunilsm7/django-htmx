from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.

class TodoQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = (
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
        return self.filter(lookups) 

class TodoManager(models.Manager):
    def get_queryset(self):
        return TodoQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    completed = models.BooleanField(default=True)

    objects = TodoManager()

    def __str__(self):
        return self.title
    
    def get_excerpt(self, total_char):
        return self.title[:total_char]
