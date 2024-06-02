
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic.edit import FormMixin

from shopOnline.models import Item
from .cart import Cart
from .forms import CartAddProductForm



def cart_add(request, product_id):
    cart = Cart(request)
    product_id = get_object_or_404(Item, id=product_id)
    print(product_id.name)

    #form = CartAddProductForm(request.POST)
    #if form.is_valid():
     #   cd = form.cleaned_data
    cart.add(product_id=product_id, quantity=1, update_quantity=False)
    a=request.session['cart']
    p=[]
    for item_id in a:
        p.append(item_id)

    print(p)
    return HttpResponse("ok")



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')



class detailCart(FormMixin,View):
    #context_object_name = "list_cart"
    #template_name = "cart/detail_cart.html"
    form_class = CartAddProductForm


    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'cart/detail_cart.html', context)

    #def get_queryset(self):
       # Cart(self.request)
        #a=self.request.session['cart']
       # item_id=[]
       # for item in a:
         #   item_id.append(int(item))

       # queryset=Item.objects.filter(pk__in=item_id)

        #print("ciao")
      #  return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve items from the database (or from wherever you get them)
        Cart(self.request)
        a = self.request.session['cart']
        item_id_cart = []
        for item in a:
            item_id_cart.append(int(item))

        items = Item.objects.filter(pk__in=item_id_cart)

        # Create a form instance for each item with its initial quantity
        forms = {}
        i=0;
        for item in items:
            # Get the initial quantity for the item (replace this with your logic)
            initial_quantity = 5
            # Instantiate the form class with the initial quantity
            form = CartAddProductForm(initial={'quantity': initial_quantity+i})
            i=i+1
            # Store the form instance in a dictionary with item ID as the key
            forms[item.id] = form


        # Add the forms dictionary to the context
        context['forms'] = forms
        context['list_cart'] = items
        return context
