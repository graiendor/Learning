import os

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Roll, Attributes
from .scripts.roll import __roll__
from .scripts.attributes import __attributes__
from django.core import serializers
from .forms import AttributesForm, RollForm
import json


class Roller(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.renderer_classes = [TemplateHTMLRenderer]
        self.template_name = "dice/dice_page.html"
        self.roll = Roll()
        self.attributes = AttributesForm()

    def get(self, request):
        return Response({'roll': self.roll, 'attributes': self.attributes})

    def post(self, request):
        if 'roll_btn' in request.POST:
            __roll__(self.roll)
        if 'submit_attributes_btn' in request.POST:
            self.attributes = AttributesForm(request.POST)
            if self.attributes.is_valid():
                print('yes')
                self.attributes.save()
        return Response({'roll': self.roll, 'attributes': self.attributes})



