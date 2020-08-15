from django.urls import path
from django.contrib.auth import views as auth_views
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

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
]