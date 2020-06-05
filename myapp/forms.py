from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
	class Meta:
		model = CountriesName
		fields = ('name', 'country_pic',)