from django.shortcuts import render, redirect
from .models import Armada, Testi, Order

from .forms import OrderForm
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
            return redirect('home')
        
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