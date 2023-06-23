from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 80)
    body = models.TextField()
    created_at = models.DateTimeField(datetime)
    image = models.ImageField(upload_to="static/assets/img", blank=True, null=True)

    def __str__ (self):
        return self.title