from dataclasses import fields
from django import forms
from.models import Profile

class profile_form(forms.ModelForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs=
    {"class":"form-control","placeholder":"Fullname"}))
    country=forms.CharField(widget=forms.TextInput(attrs=
    {"class":"form-control","placeholder":"Country"}))
    contact=forms.IntegerField(widget=forms.NumberInput(attrs=
    {"class":"form-control","placeholder":"Phone"}))
    profession=forms.CharField(widget=forms.TextInput(attrs=
    {"class":"form-control","placeholder":"Phone","size":20 }))
    class Meta:
        model=Profile
        fields={'fullname','contact','country','profession','image'}
     