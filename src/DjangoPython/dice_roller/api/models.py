from django.db import models

# Create your models here.


class Info(models.Model):
    value = models.IntegerField()
    result = models.CharField(max_length=8)
