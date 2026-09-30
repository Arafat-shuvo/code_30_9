from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'student_name', 'student_id']

    def __str__(self):
        return self.username


class ProjectModel(models.Model):
    PROJECT_STATUS_CHOICES = [
        ('Not started', 'Not started'),
        ('In progress', 'In progress'),
        ('Completed', 'Completed'),
    ]

    project_name = models.CharField(max_length=200)
    project_description = models.TextField(default='', blank=True)
    project_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_status = models.CharField(max_length=20, choices=PROJECT_STATUS_CHOICES, default='Not started')
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.project_name
    