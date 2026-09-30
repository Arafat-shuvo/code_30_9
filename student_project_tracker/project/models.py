from django.contrib.auth.models import User
from django.db import models


class ProjectModel(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user_name
    