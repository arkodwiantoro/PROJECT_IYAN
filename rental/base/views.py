from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Armada, Testi, Order
from .forms import OrderForm, UserForm
from .filters import OrderFilter

# Create your views here.
def home(request):
    armada = Armada.objects.all()
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        print('ini post')
        if form.is_valid():
            print('ini valid')
            form = form.save(commit=False)
            form.user = request.user 
            form.save()
            return redirect(reverse('notifikasi', kwargs={'pk':form.id}))
        
    context = {
        'armadas': armada,
        'form': form,
    }
    return render(request, 'base/index.html', context)


def galery(request):
    testi = Testi.objects.all()
    context = {
        'testi': testi,
    }
    return render(request, 'base/galery.html', context)

def syarat_ketentuan(request):
    context = {

    }
    return render(request, 'base/sk.html', context)


def contact(request):
    return render(request,'base/contact.html')


def adm(request):
    orders = Order.objects.all()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'orders': orders,
        'myFilter': myFilter,
    }

    return render(request, 'base/admin.html', context)

def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'email or password does not exist')

    context = {
        'page': 'login',
    }

    return render (request, 'base/login.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {
        'form': form,
        'page': 'register',
    }

    return render(request, 'base/login.html', context)

def notif(request, pk):
    order = Order.objects.get(id=pk)

    context = {
        'order': order,
    }

    return render(request, 'base/notification.html', context)