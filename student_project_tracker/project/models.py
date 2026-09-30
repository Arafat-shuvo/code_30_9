from django.db import models
from django.contrib.auth.models import AbstractUser

class user_model(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    email= models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
# Create your models here.
class ProjectModel(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.models.CharField(max_length=50)
    created_by = models.ForeignKey(user_model, on_delete = models. CASCADE) 
    created__at = models.DateField(auto_now_add= True, null = True)
    updated_at = models.DateField(auto_now =True, null=True)


    def __str__(self):
        return f'{self.name}'
    