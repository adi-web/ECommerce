
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# form used for change the quantity of a item in the cart

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int,widget=forms.Select(attrs={'onchange': 'submitQuantity(this)'}))
    # used a hidden field to save the id of the item
    item_id = forms.IntegerField(widget=forms.HiddenInput())
