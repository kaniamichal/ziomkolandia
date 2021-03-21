from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, fields
from .models import Kindergarten
from captcha.fields import CaptchaField


class KidsEnroll(ModelForm):
    captcha = CaptchaField(require_all_fields=True, label="Wpisz wynik dodawania")
    class Meta:
        model = Kindergarten
        # fields = ['kinder_name', 'user_name', 'child_name', 'class_name', 'phone_number', 'email', 'regulations']
        exclude = ['data_enrol']

        # error_messages = {'required': "Pole nie może być puste" }