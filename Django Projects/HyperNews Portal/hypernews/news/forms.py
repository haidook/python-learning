from django import forms

class NewsForm(forms.Form):
    title = forms.CharField(label='Title')
    text = forms.CharField(label='Text')

class SearchForm(forms.Form):
    q = forms.CharField(label='')