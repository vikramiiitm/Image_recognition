from django.db import models

# Create your models here.


class Image(models.Model):
    """
    Image model containing Image and detected objects
    """
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    objects_detected = models.CharField(null=True, blank=True, max_length=1024)
    timestamp = models.DateField(null=True, blank=True)