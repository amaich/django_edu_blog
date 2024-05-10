from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title