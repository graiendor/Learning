from django.db import models

# Create your models here.


class Roll(models.Model):
    value = models.IntegerField(editable=False)
    result = models.CharField(editable=False, max_length=8)
    
    class Meta:
        pass