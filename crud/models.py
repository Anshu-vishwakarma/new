from django.db import models

class TaskData(models.Model):
    task=models.CharField(max_length=20)
    date=models.DateField()
    dec=models.TextField()
