from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_order/<int:pk>', views.create_order, name='create_order'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('user-page/', views.user_page, name='user-page'),
    path('account/', views.accountSettings, name='account'),
    
]