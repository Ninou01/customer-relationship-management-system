from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import inlineformset_factory
from .filters import OrderFilter
from .models import Customer, Product, Order, Tag
from .froms import OrderForm, CreateUserForm

# Create your views here.

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    

    context = {
        'customer':customer,
        'orders':orders,
        'myfilter':myfilter,
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
            return redirect('/customer/%s'%pk)
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


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            user = form.cleaned_data.get('username')
            messages.success(request, 'accout was created for ' + user)

            return redirect('/dashboard')

    else:
        form = CreateUserForm()        

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('/login')