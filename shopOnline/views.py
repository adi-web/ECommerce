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
from comment.models import CommentItem
from shopOnline.forms import AddQuantity

from shopOnline.models import Item, Categories


class listofItem(ListView):

    context_object_name = "list_items"
    template_name = "shopOnline/shop.html"

    def get_queryset(self, *args, **kwargs):

        #look in the url id for categori
        pk_list = self.kwargs

        #print(pk_list)

        #if i want all the category todisplay i do not have id in the url
        if pk_list =={}:
            queryset = Item.objects.filter()
        else:
            queryset = Item.objects.filter(categories=pk_list['pk'])
            print(queryset.values())

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_list = self.kwargs
        if pk_list =={}:
            context["nameCategory"]="All Category"
        else:
            queryC=Item.objects.filter(pk=pk_list['pk']).select_related("categories").all()

            for item in queryC:
                context["nameCategory"] = item.categories.name

        item_id_cart = []
        Cart(self.request)
        if self.request.session['cart']:
            session_cart = self.request.session['cart']

            for item in session_cart:
                item_id_cart.append(int(item))

            print(item_id_cart)
            context["cart_id"]=item_id_cart

        print("user e ")
        print(self.request.user.pk)
        return context





class detailView(FormMixin,DetailView):
    model = Item
    context_object_name = "detail_item"
    template_name = "shopOnline/detail_Item.html"
    form_class = AddQuantity

    def get_queryset(self):

        return Item.objects.all()

    #when i add the quantity i riderct to the same page html
    def get_success_url(self):
        return reverse('detail_item', kwargs={'pk': self.object.pk})


    #add new Quantity i take the quantity and i save in the session cart
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = AddQuantity(request.POST)
        print("questo è form")



        #if form.is_valid():

        cart = Cart(self.request)
        session_item = self.request.session['cart']
        for id_item in request.session['cart']:
            if id_item == str(self.object.pk):
                if form.is_valid():
                    form_detail = form.cleaned_data
                    if form_detail["quantiyt_item"]< session_item[id_item]['quantity']:
                        cart.add(product_id=self.object.pk, quantity=session_item[id_item]['quantity'] - 1, update_quantity=True)
                    else:
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

                context['itemcart']=session_item[id_item]["quantity"]
        #queryCommet=CommentItem.objects.filter(itemComment_id=self.object.pk)
        queryCommet = CommentItem.objects.all()

        comment=[]
        for c in queryCommet:
            comment.append(c)



        print("dopo for")
        for o in comment:
            print(o.pk)
#        context['names']=queryCommet.get().customer
        context['comments'] = comment
        print('comments')
        print(queryCommet.values())
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


