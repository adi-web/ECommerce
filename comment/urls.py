from django.contrib.auth.decorators import login_required
from django.urls import path
# Create your views here.
from comment.views import CommentCreateView, CommentDeleteView, CommentUpdateView

urlpatterns=[

    path('<int:pk>/item/',login_required(CommentCreateView.as_view()),name='comment_create'),

    path("<int:itemId>/idComment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),

    path("<int:itemId>/idComment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment_update"),

]
