from django.urls import path
from django.views.generic import RedirectView

from .views import listofItem, detailView

urlpatterns=[

    path('item/<int:pk>',detailView.as_view(),name='detail_item'),
]
