from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from.models import *
class do_form(forms.ModelForm):
    # # error_css_class='error_field'
    # # required_css_class='required_field'
    title=forms.CharField(widget=forms.TextInput(attrs=
    {"class":"form-control","placeholder":"Title"}))
    duetime=forms.IntegerField(widget=forms.NumberInput(attrs=
    {"class":"form-control","placeholder":"Duetime"}))
    # description=forms.Textarea(widget=forms.TextInput(attrs=
    # {"class":"form-control","placeholder":"Description"}))
    class Meta():
        model=Todo
        fields={'title','description','completed','consumed_time','duetime'}

        # widgets= {
        #     'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
        #     'description' : forms.Textarea(attrs={'class':'textarea','placeholder':'Description'}),
        #     'title' : forms.TextInput(attrs={'class':'input','placeholder':'title'})
        # }