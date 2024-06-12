from django.contrib.auth.decorators import login_required
from django.urls import path
# Create your views here.
from .views import listOrder

urlpatterns=[

    path('',login_required(listOrder.as_view()),name='detail_orders'),

]
