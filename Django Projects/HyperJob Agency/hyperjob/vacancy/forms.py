from django import forms

class NewForm(forms.Form):
    description = forms.CharField()