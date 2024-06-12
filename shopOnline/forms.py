from django import forms

class AddQuantity(forms.Form):
    quantiyt_item = forms.IntegerField()
