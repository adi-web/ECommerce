from django.urls import path

from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import  detailCart, removeItem

urlpatterns=[
    # path use to display the cart
    path('', detailCart.as_view(), name='cart_detail'),

    # path use for remove a item from the cart
    path('remove/<int:product_id>',removeItem.as_view(),name='remove_item')
]
