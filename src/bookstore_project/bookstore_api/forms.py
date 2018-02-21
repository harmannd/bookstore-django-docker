from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search Text', max_length=100)