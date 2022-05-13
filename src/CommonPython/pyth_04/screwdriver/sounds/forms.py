from .models import Sound
from django.forms import ModelForm
import fleep


class SoundForm(ModelForm):
    class Meta:
        model = Sound
        fields = ['Submit it']

    def is_sound(self, file) -> bool:
        check: bool = False
        sound = fleep.get(file.read(128))
        print(sound.type)
        if sound.type == ['audio']:
            check = True
        return check


