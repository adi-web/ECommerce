from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView

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





class deleteItem(DeleteView):
    template_name = "delete_Item_order.html"
    model = OrderItem
    success_url = reverse_lazy('detail_orders')





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

        totpay= self.getTotPay()
        cart=Cart(self.request)
        cartItem = self.request.session['cart']
        order, created = Order.objects.get_or_create(pk=modelO.pk)
        order.userOrder=self.request.user
        order.totpay=totpay[0]
        order.save()


        # save in the DB the info of the order an item
        for item in cartItem:
           itemOrder, created = Item.objects.get_or_create(pk=item)
           OrderItem.objects.create(item=itemOrder,order=order,quantity=cartItem[str(item)]['quantity'],payQuantity=totpay[1].get(int(item))*cartItem[str(item)]['quantity'])

        cart.clear()
        return render(request,"success.html")



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryOrder = OrderItem.objects.order_by('-order_id').select_related('order').filter(order__userOrder_id=self.request.user.pk)
        context['order']=queryOrder

        return context



    def getTotPay(self):
        itemCart = self.request.session['cart']
        item_id_cart = []
        for item in itemCart:
            item_id_cart.append(int(item))

        items = Item.objects.filter(pk__in=item_id_cart)
        totpay=0
        payItem={}
        for i in items:
            totpay = totpay + int(itemCart[str(i.id)]['quantity']) * i.price
            payItem[i.id]=i.price

        return totpay,payItem
