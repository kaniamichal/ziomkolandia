from django.forms import ModelForm
from django import forms
from .models import Kindergarten, Camp, DayCamp
from captcha.fields import CaptchaField


class KidsEnroll(ModelForm):
    captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik działania")

    class Meta:
        model = Kindergarten
        exclude = ['data_enrol']


class CampEnroll(ModelForm):
    captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik działania")

    class Meta:
        model = Camp
        exclude = ['data_enrol']


class DayCampEnroll(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DayCampEnroll, self).__init__(*args, **kwargs)
        self.fields['receiving_person_2'].required = False
        self.fields['receiving_person_2'].initial = '-----'
        self.fields['relationship_child_2'].required = False
        self.fields['relationship_child_2'].initial = '-----'
        self.fields['phone_receiving_2'].required = False
        self.fields['phone_receiving_2'].initial = '-----'
        self.fields['receiving_person_3'].required = False
        self.fields['receiving_person_3'].initial = '-----'
        self.fields['relationship_child_3'].required = False
        self.fields['relationship_child_3'].initial = '-----'
        self.fields['phone_receiving_3'].required = False
        self.fields['phone_receiving_3'].initial = '-----'

    captcha = CaptchaField(label="Wpisz wynik działania")

    class Meta:
        model = DayCamp
        exclude = ['data_enrol']


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=200, required=True)
    contact_title = forms.CharField(max_length=200, required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    # class Meta:
    #     fields = ('contact_name', 'contact_title', 'contact_email', 'content')
    #     widgets = {
    #         'contact_name': forms.TextInput(attrs={'class': 'form-control', }),
    #         'contact_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł'}),
    #         'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    #         'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Treść wiadoości'}),
    #
    #     }
# captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik działania")
