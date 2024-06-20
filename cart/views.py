
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic.edit import FormMixin

from shopOnline.models import Item
from .cart import Cart
from .forms import CartAddProductForm


class removeItem(View):

    def get_success_url(self):
        return reverse('cart_detail')

    def post(self, request, *args, **kwargs):
        self.kwargs['product_id']
        cart = Cart(request)
        product = get_object_or_404(Item, id=self.kwargs['product_id'])
        cart.remove(product)
        return HttpResponseRedirect(self.get_success_url())



class detailCart(FormMixin,View):
    form_class = CartAddProductForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'cart/detail_cart.html', context)

    def get_success_url(self):
        return reverse('cart_detail')


    def post(self, request, *args, **kwargs):

        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cart = Cart(self.request)
            form_detail = form.cleaned_data
            cart.add(product_id=form_detail["item_id"], quantity=form_detail["quantity"], update_quantity=True)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Cart(self.request)
        a = self.request.session['cart']

        item_id_cart = []
        for item in a:
            item_id_cart.append(int(item))

        items = Item.objects.filter(pk__in=item_id_cart)

        # Create a form instance for each item with his initial quantity
        forms = {}
        i=0;
        session_item = self.request.session['cart']
        pay=0
        for item in items:

            form = CartAddProductForm(initial={'quantity': session_item[str(item.id)]['quantity'],'item_id':item.id})
            pay=pay+int(session_item[str(item.id)]['quantity'])*item.price
            print("da pagare")
            print(pay)
            i=i+1

            forms[item.id] = form
        context['pay']=pay
        context['forms'] = forms
        context['list_cart'] = items
        return context
