from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 80)
    body = models.CharField(max_length = 300000)
    created_at = models.DateTimeField(datetime)