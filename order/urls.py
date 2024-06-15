from django.contrib.auth.decorators import login_required
from django.urls import path
# Create your views here.
from .views import listOrder, processOrder, orderList

urlpatterns=[

    path('',login_required(listOrder.as_view()),name='detail_orders'),
    path('process/',login_required(processOrder.as_view()),name='process_cart'),
    path('detailOrder/<int:pk>',login_required(orderList.as_view()),name='item_order'),

]
