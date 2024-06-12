from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView

from shopOnline.models import Item


class listOrder(ListView):
    model = Item
    context_object_name = "ciao"
    template_name = "order.html"
    queryset = Item.objects.all()

