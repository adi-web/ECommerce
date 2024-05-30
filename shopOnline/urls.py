from django.urls import path
from . import views
from .views import listofItem, detailView

urlpatterns=[
    path('',listofItem.as_view(),name='shop'),
    path('item/<int:pk>',detailView.as_view(),name='detail_item'),

]
