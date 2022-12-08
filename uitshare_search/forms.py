from django import forms

class SearchForm(forms.ModelForm):
    search = forms.CharField()