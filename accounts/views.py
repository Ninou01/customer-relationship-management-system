from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from .filters import OrderFilter
from .models import Customer, Product, Order, Tag
from .froms import OrderForm, CreateUserForm
from .decorators import unauthenticated_user, allowed_users, adminonly

# Create your views here.


@login_required(login_url='/login/')
@adminonly
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


@login_required(login_url='/login/')
@allowed_users(['admin'])
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


@login_required(login_url='/login/')
@allowed_users(['admin'])
def products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'accounts/product.html', context)


@login_required(login_url='/login/')
@allowed_users(['admin'])
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


@login_required(login_url='/login/')
@allowed_users(['admin'])
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


@login_required(login_url='/login/')
@allowed_users(['admin'])
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/dashboard')

    context = {
        'item':order
    }
    return render(request, 'accounts/delete_order.html', context)


@unauthenticated_user
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


@unauthenticated_user
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


@login_required(login_url='/login/')
def user_page(request):
    return render(request, 'accounts/user-page.html')

# if you want to use a customize 404 page
# set DEBUG = False and ALLOWED_HOSTS = ['localhost'] in setings.py
# and add handler404 = 'accounts.views.notfound' this to 'crm1/urls.py'
# and use this view function below

# def notfound(request, exception):
#     return render(request,'accounts/404.html')