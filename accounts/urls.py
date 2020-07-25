from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('products', views.products, name='products'),
    path('dashboard', views.dashboard, name='dashboard'),
]