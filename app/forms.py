from django import forms
from .models import *
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ('patient','doctor', 'document', )