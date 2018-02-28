from django import forms

from .models import Book


class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search'}
        ),
        required=False
    )
    category = forms.ChoiceField(
        label='',
        choices=[(1, 'Title'), (2, 'Author')],
        required=False
    )


class FilterForm(forms.Form):
    file_type = forms.MultipleChoiceField(
        choices=Book.FILE_TYPES,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    language = forms.MultipleChoiceField(
        choices=Book.LANGUAGES,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
