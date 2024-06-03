from django.urls import path

from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import cart_add, detailCart, removeItem

urlpatterns=[
    path('', detailCart.as_view(), name='cart_detail'),
    path('remove/<int:product_id>',removeItem.as_view(),name='remove_item')
]
