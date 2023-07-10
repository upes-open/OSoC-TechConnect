from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    submitted_by = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)