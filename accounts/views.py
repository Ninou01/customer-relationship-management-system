from django.shortcuts import render, redirect
from .models import Customer, Product, Order, Tag
from .froms import OrderForm

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

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = OrderForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/create_update_order.html', context)

def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = OrderForm(instance=order)
    context = {
        'form':form
    }
    return render(request, 'accounts/create_update_order.html', context)

def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/dashboard')

    context = {
        'item':order
    }
    return render(request, 'accounts/delete_order.html', context)

