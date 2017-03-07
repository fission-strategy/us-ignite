from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(max_length=50, label='Search', required=False)
    sector = forms.CharField(max_length=100, label='Sector', required=False)
    program = forms.CharField(max_length=100, label='Program', required=False)
    order = forms.CharField(max_length=4, label='Order', required=False)
