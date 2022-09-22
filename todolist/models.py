from django.db import models
from django.conf import settings
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.TextField()