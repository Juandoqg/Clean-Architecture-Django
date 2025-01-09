from django.urls import path
from myapp.presentation.views.user_views import create_user_view
from django.shortcuts import render
urlpatterns = [
    path('', create_user_view, name='create_user'),
    path('success/', lambda request: render(request, "success.html"), name='success_page'),
]