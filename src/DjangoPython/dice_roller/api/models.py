from django.db import models
from django.core.validators import int_list_validator
# Create your models here.


class Roll(models.Model):
    # value = models.IntegerField(default=1)
    value = models.CharField(max_length=50)
    result = models.CharField(max_length=8, default='')


class Attributes(models.Model):
    strength = models.IntegerField(default=1)
    strength_check = models.BooleanField(default=False)

    dexterity = models.IntegerField(default=1)
    dexterity_check = models.BooleanField(default=False)

    stamina = models.IntegerField(default=1)
    stamina_check = models.BooleanField(default=False)

    charisma = models.IntegerField(default=1)
    charisma_check = models.BooleanField(default=False)

    manipulation = models.IntegerField(default=1)
    manipulation_check = models.BooleanField(default=False)

    composure = models.IntegerField(default=1)
    composure_check = models.BooleanField(default=False)

    intelligence = models.IntegerField(default=1)
    intelligence_check = models.BooleanField(default=False)

    wits = models.IntegerField(default=1)
    wits_check = models.BooleanField(default=False)

    resolve = models.IntegerField(default=1)
    resolve_check = models.BooleanField(default=False)