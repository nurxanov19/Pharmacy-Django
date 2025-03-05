from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm
from .models import Medicine
import datetime


class MedicineForm(ModelForm):

    class Meta:
        model = Medicine
        fields = '__all__'

    # def clean_exp_date(self):
    #     exp_date = self.cleaned_data['expiration_date']
    #
    #     if exp_date < datetime.now():
    #         raise ValidationError('This Medicine is expired')
    #
    #     return exp_date

