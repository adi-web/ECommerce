from venv import logger

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from comment.models import CommentItem
from shopOnline.models import Item


class CommentCreateView(CreateView):  # new
    # con questo indende di creare un modello di article
    model = CommentItem
    template_name = "comment_new.html"

    fields = (
        "description",
    )

    def get_success_url(self):
        return reverse_lazy('detail_item', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']  # Pass the pk to the template context
        return context

    def form_valid(self, form):
        item_id = self.kwargs.get('pk')
        print("itemid")
        print(item_id)
        try:
            item = Item.objects.get(pk=item_id)
            print(item_id)
        except Item.DoesNotExist:
            raise Http404("Item does not exist")
        form.instance.itemComment = item
        form.instance.customer = self.request.user
        return super().form_valid(form)


class CommentDeleteView(DeleteView):  # new
    model = CommentItem
    template_name = "comment_delete.html"
    def get_success_url(self):
        return reverse_lazy('detail_item', kwargs={'pk': self.kwargs['itemId']})


class CommentUpdateView(UpdateView):
    model = CommentItem
    fields = (
        "description",
    )
    template_name = "comment_update.html"

    def get_success_url(self):
        return reverse_lazy('detail_item', kwargs={'pk': self.kwargs['itemId']})
