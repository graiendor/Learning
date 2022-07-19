from django.forms import ModelForm
from .models import Roll, Attributes


class RollForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RollForm, self).__init__(*args, **kwargs)
        self.fields['value'].disabled = True
        self.fields['result'].disabled = True
    class Meta:
        model = Roll
        fields = ['value', 'result']


class AttributesForm(ModelForm):
    class Meta:
        model = Attributes
        fields = ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'composure', 'intelligence', 'wits', 'resolve']