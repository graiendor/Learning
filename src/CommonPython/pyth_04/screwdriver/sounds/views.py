from calendar import c
from xml.dom import ValidationErr
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django import forms
import fleep

# Create your views here.\


class SoundInstance:
    name = 'yep'


class SoundGetForm(forms.Form):
    sound = forms.FileField(help_text="Enter the sound")
    fields = ('title', 'text')


def index(request):
    # return HttpResponse("Hello, world. You're at the sounds index.")
    # sound_instance = get_object_or_404(SoundInstance, pk=pk)

    if request.method == 'POST':
        form = SoundGetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            line = request.FILES.readlines()

            return HttpResponse("{line}")
    else:
        form = SoundGetForm()
    context = {
        'form': form,
    }
    return render(request, 'sounds/haha.html', context)
