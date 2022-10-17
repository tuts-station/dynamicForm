from django import forms
from .models import Field, FormName

CHOICES = (
    ('text','Text'),
    ('textarea','Textarea'),
    ('radio','Radio'),
    ('checkbox','Checkbox'),
    ('file','File'),
    ('date','Date'),
)
VALIDATION_CHOICES = [
    ('required', 'Required'),
]

class FieldForm(forms.ModelForm):

    field_type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=VALIDATION_CHOICES,
    )
    type = forms.ChoiceField(choices=CHOICES,
                                    widget=forms.Select(attrs={'class': 'form-control selectfield',
                                }))
    label = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Label',
                                                         'class': 'form-control form-label',
                                                         }))
    more_field = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': '',
                                                         'class': 'form-control fieldsname',
                                                         }))

    class Meta:
        model = Field
        fields = ['type','label','more_field','field_type',]


class FormNameForm(forms.ModelForm):

    name = forms.CharField(max_length=100,required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Form Name',
                                                         'class': 'form-control',
                                                         }))

    class Meta:
        model = FormName
        fields = ['name',]
