from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('products', views.products, name='products'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_order', views.create_order, name='create_order'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
]