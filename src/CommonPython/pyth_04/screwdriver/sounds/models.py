from django.db import models


# Create your models here.

class Sound(models.Model):
    body = models.FileField(upload_to='sounds/')
    body.name = 'Submit it'
