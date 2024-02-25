# videostream/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=20, default='')  # Provide a default value
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
