
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
                                      widget=forms.Select(attrs={'onchange': 'submitQuantity(this)'}))

    item_id = forms.IntegerField(widget=forms.HiddenInput())
