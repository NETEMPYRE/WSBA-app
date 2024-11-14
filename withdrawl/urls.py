from django.urls import path
from . import views

urlpatterns = [
    path('withdrawl/', views.post_request, name='post_request'),
    path('withdrawls/', views.get_request, name='get_request'),
]