from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    choices = (('m','Maths'),('s','Software'))
    post_topic = models.CharField(max_length=10,choices=choices, default='m')
    post_image = models.ImageField(
            upload_to=settings.UPLOADS_URL[1:] + "pics/",
            default =settings.UPLOADS_URL[1:] + 'pics/no-img.jpg')
    def __str__(self):
        return self.post_title

class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title
