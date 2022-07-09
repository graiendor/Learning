import random

from rest_framework import views
from django.http import HttpResponse, JsonResponse
from .models import Roll
from .serializers import RollSerializer
import random

# Create your views here.

def roll_data(request):
    if request.method == 'GET':
        roll = Roll.objects.all()
        __make_roll__(roll)
        serializer = RollSerializer(roll)
        return JsonResponse(serializer.data, safe=False)

def __make_roll__(roll):
    roll.value = random.randint(1, 10)
    roll.result = "SUCCESS" if roll.value >= 6 else "FAIL"
