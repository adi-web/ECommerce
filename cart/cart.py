from decimal import Decimal
from django.conf import settings

from shopOnline.models import Item


class Cart():

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product_id, quantity, update_quantity=False):

        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':quantity }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):

        self.session.modified = True



    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()



    def clear(self):

        del self.session[settings.CART_SESSION_ID]
        self.save()



