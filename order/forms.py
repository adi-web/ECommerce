from django import forms

from order.models import Order


class OrderForms(forms.ModelForm):

    class Meta:
        model= Order
        fields=('phoneNumber','addressOrder','noteOrder')
