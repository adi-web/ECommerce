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

    def __init__(self, *args, **kwargs):
        super(OrderForms, self).__init__(*args, **kwargs)
        self.fields['phoneNumber'].required = True
        self.fields['addressOrder'].required = True


