from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    expires_at = models.DateTimeField()