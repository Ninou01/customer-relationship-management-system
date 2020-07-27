from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
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

def create_order(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, 
        Order, 
        fields = ['product','status'],
        extra=6
        )
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/dashboard')
    else:
        formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    context = {
        'formset':formset
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

