import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django import forms
from .models import Certificate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create a form for edit path
class CertificateModelForm(forms.ModelForm):
    leave_date = forms.DateField(widget=forms.DateInput(attrs={'id':'datepicker', 'placeholder': 'Date of departure'}), label='Date of departure')
    leave_hour = forms.TimeField(widget=forms.TextInput(attrs={'id':'timepicker', 'placeholder': 'Departure time'}), label='Departure time')
    return_hour = forms.TimeField(widget=forms.TextInput(attrs={'id':'timepicker1', 'placeholder': 'Arrival time'}), label='Arrival time', required=False)

    class Meta:
        model = Certificate
        fields = ['leave_date', 'leave_hour', 'return_hour']


    def clean_leave_date(self):
        data = self.cleaned_data['leave_date']

        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid previous date'))

        return data

