from django.db import models
from task.models import TaskModel

class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=255)
    tasks = models.ManyToManyField(TaskModel)