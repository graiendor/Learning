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
        fields = ['strength', 'strength_check', 'charisma', 'charisma_check', 'intelligence', 'intelligence_check', 'dexterity', 'dexterity_check',
                  'manipulation', 'manipulation_check', 'wits', 'wits_check', 'stamina', 'stamina_check',  'composure', 'composure_check', 'resolve', 'resolve_check']