from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Roll, Attributes
from .scripts.roll import __roll__
from .scripts.attributes import __attributes__

class Roller(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "dice/dice_page.html"
    roll = Roll.objects.all()
    attributes = Attributes.objects.all()

    def get(self, request):

        print(request.GET)
        if request.GET.get('roll_btn'):
            __roll__(self.roll)
        if request.GET.get('submit_attributes_btn'):
            __attributes__(self.attributes, request)
        return Response({'roll': self.roll, 'attributes': self.attributes})


