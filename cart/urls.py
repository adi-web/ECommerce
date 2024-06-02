from django.urls import path

from django.urls import path
from django.views.generic import RedirectView

from . import views
from .views import cart_add, detailCart

urlpatterns=[
    path('carello/', detailCart.as_view(), name='cart_detail'),

]
