# zomato/forms.py

from django import forms

class AddDishForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(decimal_places=2)
    available = forms.BooleanField(required=False)
