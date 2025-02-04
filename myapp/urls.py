from django.urls import path
from myapp.presentation.views.user_views import create_user_view
from django.shortcuts import render
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/users/create/', create_user_view, name='create_user'),   
    path('success/', lambda request: render(request, "success.html"), name='success_page'),
]