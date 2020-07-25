from django.shortcuts import render
from .models import Customer, Product, Order, Tag

# Create your views here.

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context = {
        'customer':customer,
        'orders':orders,
    }
    return render(request, 'accounts/customer.html', context)


def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    delivered = Order.objects.filter(status='Delivered')
    pending = Order.objects.filter(status='Pending')

    context = {
        'orders':orders,
        'customers':customers,
        'delivered':delivered,
        'pending':pending,
    }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'accounts/product.html', context)

