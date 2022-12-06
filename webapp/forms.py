from django import forms
from .models import Products


class NewProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}), help_text='Enter name of the product.')

    class Meta:
        model = Products
        fields = ['name']
