from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    description = models.TextField(max_length=360)
    author = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % (self.title)