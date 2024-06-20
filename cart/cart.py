
from django.conf import settings

# class tha i use to save or create a session for the cart
# there is the method add for add to the session an item with the quantity
# save is to save the session , clear to delete the session , remove is for remove an item from the session

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



