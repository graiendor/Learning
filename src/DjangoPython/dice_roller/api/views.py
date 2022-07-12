from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from .models import Info
from .scripts.roll import __roll__

class Roller(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "dice/dice_page.html"

    def get(self, request):
        roll = Info.objects.all()
        __roll__(roll)
        return Response({'data': roll})


