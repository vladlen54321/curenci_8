from django import forms
from currency.models import ContactUs, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'email_to',
            'subject',
            'message',
        )

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
        )