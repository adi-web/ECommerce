from django import forms

from order.models import Order

# form used to add at the order extra information

class OrderForms(forms.ModelForm):

    class Meta:
        model= Order
        fields=('phoneNumber','addressOrder','noteOrder')
        labels = {
            "phoneNumber": "Phone number",
            "addressOrder": "Address to ship",
            "noteOrder": "Note for the rider",
        }
