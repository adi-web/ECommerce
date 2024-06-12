from django.urls import path
from django.views.generic import RedirectView

from .views import listofItem, detailView

urlpatterns=[

    path('item/<int:pk>',detailView.as_view(),name='detail_item'),

    #path('item/<int:product_id>', RedirectView.as_view(url=' ', permanent=False), name='cart_detail2'),
    #path('item',detailView.as_view(),name='detail_item'),

]
