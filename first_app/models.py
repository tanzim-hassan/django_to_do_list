from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=25)
    task_description = models.CharField(max_length=75)
    is_completed = models.BooleanField(default=False)
    task_number=models.IntegerField(primary_key=True)