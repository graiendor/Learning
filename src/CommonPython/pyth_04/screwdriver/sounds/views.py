import os
from calendar import c
from xml.dom import ValidationErr
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import SoundForm
from django.core.files.storage import FileSystemStorage

# Create your views here.\


def index(request):
    # return HttpResponse("Hello, world. You're at the sounds index.")
    # sound_instance = get_object_or_404(SoundInstance, pk=pk)
    path = '/Users/ereva/Pyth/src/CommonPython/pyth_04/screwdriver/media/sounds'
    img_list = os.listdir(path)
    print(img_list)
    if request.method == 'POST':
        form = SoundForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_sound(request.FILES['Submit it']):
                form.save()
    else:
        form = SoundForm()
    return render(request, 'sounds/haha.html', {'form': form, 'images': img_list})
