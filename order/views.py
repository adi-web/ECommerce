from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from cart.cart import Cart
from order.forms import OrderForms
from order.models import Order, OrderItem
from shopOnline.models import Item


class orderList(ListView):
    context_object_name = "list_itemsOrder"
    template_name = "detailOrder.html"

    def get_queryset(self, *args, **kwargs):
        pk_list=self.kwargs
        itemList=OrderItem.objects.filter(order=pk_list['pk'])
        print(itemList)
        return itemList



class processOrder(CreateView):
    form_class = OrderForms
    template_name = 'processOrder.html'

class listOrder(ListView):
    model = Item
    template_name = "order.html"



    def post (self, request, *args, **kwargs):

        form=OrderForms(request.POST)
        if form.is_valid():
            modelO=form.save()
            print(modelO.pk)

        print("entrato")
        totpay= self.getTotPay()
        print(totpay)
        cart=Cart(self.request)
        a = self.request.session['cart']
        order, created = Order.objects.get_or_create(pk=modelO.pk)
        order.userOrder=self.request.user
        order.totpay=totpay
        order.save()
        print(order.phoneNumber)

        for item in a:
           itemOrder, created = Item.objects.get_or_create(pk=item)
           OrderItem.objects.create(item=itemOrder,order=order,quantity=a[str(item)]['quantity'])
        cart.clear()
        return render(request,"success.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryOrder=Order.objects.filter(userOrder_id=self.request.user.pk)
        context['order']=queryOrder

        return context

    def getTotPay(self):
        itemCart = self.request.session['cart']
        item_id_cart = []
        for item in itemCart:
            item_id_cart.append(int(item))

        items = Item.objects.filter(pk__in=item_id_cart)
        totpay=0
        for i in items:
            totpay = totpay + int(itemCart[str(i.id)]['quantity']) * i.price


        return totpay
