import self as self
from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from django.views.generic import TemplateView, ListView, DetailView

from shopOnline.models import Item


class listofItem(ListView):

    context_object_name = "list_items"
    queryset=Item.objects.all()
    template_name = "shop.html"

class detailView(DetailView):
    model = Item
    context_object_name = "detail_item"
    queryset = Item.objects.filter()
    template_name = "detail_Item.html"


