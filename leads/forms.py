from django import forms
from .models import Leads
from django.forms.widgets import TextInput,NumberInput,Select 
class LeadModelForm(forms.ModelForm):
    class Meta:
        model=Leads
        fields=(
            'first_name',
            'last_name',
            'age',
            'agent'
        )
        widgets={
            'first_name':TextInput(attrs={'class':'form-control'}),
            'last_name':TextInput(attrs={'class':'form-control'}),
            'age':NumberInput(attrs={'class':'form-control'}),
            'agent':Select(attrs={'class':'form-control'})

        }


class LeadForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    age=forms.IntegerField(min_value=0)
