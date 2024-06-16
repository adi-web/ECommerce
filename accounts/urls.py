from django.urls import path
from django.contrib.auth import views
from .views import SignUpView, MyLoginView

urlpatterns=[
    path("signup/",SignUpView.as_view(),name="signup"),
    path("login/", MyLoginView.as_view(), name="login"),
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

]
