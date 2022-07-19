from django.db import models
from django.core.validators import int_list_validator
# Create your models here.


class Roll(models.Model):
    # value = models.IntegerField(default=1)
    value = models.CharField(max_length=50)
    result = models.CharField(max_length=8, default='')


class Attributes(models.Model):
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)