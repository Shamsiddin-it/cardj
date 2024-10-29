from .models import *
from django import forms
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('user', 'company', 'name', 'year', 'price', 'image')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'image')