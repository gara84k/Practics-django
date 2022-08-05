from django.db import models

# Create your models here.
class Task(models.Model):
    tipo = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)