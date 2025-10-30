from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    title_data = models.CharField(max_length=200)
    desc_data = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class HistoryModel(models.Model):
    title_data = models.CharField(max_length=200)
    desc_data = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    original_id = models.IntegerField(default=0)