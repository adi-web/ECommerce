import self as self
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from cart import cart
from cart.cart import Cart
from cart.forms import CartAddProductForm

from shopOnline.models import Item


class listofItem(ListView):

    context_object_name = "list_items"
    queryset=Item.objects.all()
    template_name = "shop.html"

class detailView(DetailView):
    model = Item
    context_object_name = "detail_item"
    template_name = "detail_Item.html"
    #form_class = CartAddProductForm

    def get_queryset(self):
        return Item.objects.all()

    #when i change the quantity i riderct to the same page html
    def get_success_url(self):
        return reverse('detail_item', kwargs={'pk': self.object.pk})


    #add new Quantity i take the quantity and i save in the session cart
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #form = self.get_form()


        #if form.is_valid():

        cart = Cart(self.request)
        session_item = self.request.session['cart']
        for id_item in request.session['cart']:
            print(self.object.pk)
            print("c")
            if id_item == str(self.object.pk):
                print("entra")
                cart.add(product_id=self.object.pk, quantity=session_item[id_item]['quantity']+1, update_quantity=True)
                return HttpResponseRedirect(self.get_success_url())

        cart.add(product_id=self.object.pk, quantity=1, update_quantity=True)
        print(request.session['cart'])
        return HttpResponseRedirect(self.get_success_url())
        #else:
           # return self.form_invalid(form)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['form'] = self.get_form()
        #context['form']
        session_item = self.request.session['cart']
        for id_item in self.request.session['cart']:
            print("entr")
            if id_item == str(self.object.pk):
                context['prova']="Item added in the Cart , There are in the Cart :  "
                context['itemcart']=session_item[id_item]["quantity"]

        return context

    #take from the cart the actual quantity (or default quantity if i did not choose) to display in detail_item
    #def get_initial(self):
       # initial = super().get_initial()
        #cart = Cart(self.request)
        #session_item=self.request.session['cart']
        #print(session_item)
        #quantity_item=0
        #for item_s in self.request.session['cart']:
          #    if(self.object.pk==int(item_s)):
                #  quantity_item=session_item[item_s]['quantity']
                #print(session_item[item_s]['quantity'])

        #print(quantity_item)
        #initial['quantity'] = quantity_item
        #return initial


