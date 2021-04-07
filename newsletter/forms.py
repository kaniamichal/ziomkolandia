from django import forms
from django.forms import ModelForm

from .models import Join


class JoinForm(ModelForm):
    newsletter_email = forms.EmailField(label='',
                                        widget=forms.EmailInput(
                                            attrs={
                                                'placeholder': 'Add your email',
                                                'class': 'form-control mb-2 text-center',
                                            }
                                        ))

    class Meta:
        model = Join
        exclude = ['newsletter_timestamp']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('newsletter_email')
        qs = Join.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Twój adres mailowy już jest dodany")
        return email
