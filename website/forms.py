from django.forms import ModelForm
from django import forms
from django.utils.safestring import mark_safe

from .models import Kindergarten, Camp, DayCamp
from captcha.fields import CaptchaField


# form from model to enroll kids to a specjal lesson in a few kindergarten
class KidsEnroll(ModelForm):

    def __init__(self, *args, **kwargs):
        super(KidsEnroll, self).__init__(*args, **kwargs)
        self.fields['regulations_image'].required = False
        self.fields['regulations_image'].initial =  False

    captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik działania")

    class Meta:
        model = Kindergarten
        labels = {
            "regulations": mark_safe(
                'Zapoznałem/am się i akceptuję <a href="/regulamin" target="_blank"> regulamin</a> '
                'oraz <a href="/polityka-prywatnosci" target="_blank">politykę prywatności</a>'),
            "regulations_image": mark_safe(
                'Wyrażam zgodę na nieodpłatne utrwalenia i publikowanie wizerunku mojego dziecka <br/> (w formie '
                'fotograficznej i/lub filmowej) utrwalonego podczas zajęć organizowanych przez <br/> Ziomkosferę w celach '
                'promocyjnej działalności Administratora za pośrednictwem dowolnego medium. <br/>Zgodę mogę odwołać w '
                'każdym momencie. (ZGODA NIEOBOWIĄZKOWA)')
        }
        exclude = ['data_enrol']

# form from model to enroll kids to camp
class CampEnroll(ModelForm):
    captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik działania")

    class Meta:
        model = Camp
        labels = {
            "regulations": mark_safe(
                'Zapoznałem/am się i akceptuję <a href="/regulamin" target="_blank"> regulamin</a>'
                ' oraz <a href="/polityka-prywatnosci" target="_balnk">politykę prywatności</a>')
        }
        exclude = ['data_enrol']

# form from model to enroll kids to day camp
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
        labels = {
            "regulations": mark_safe(
                'Zapoznałem/am się i akceptuję <a href="/regulamin" target="_blank"> regulamin</a> '
                'oraz <a href="/polityka-prywatnosci" target="_blank">politykę prywatności</a>')
        }
        exclude = ['data_enrol']

# contact form
class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=200, required=True)
    contact_title = forms.CharField(max_length=200, required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
