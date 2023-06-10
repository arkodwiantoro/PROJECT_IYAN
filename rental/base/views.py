from django.shortcuts import render

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'base/index.html', context)


def galery(request):
    context = {

    }
    return render(request, 'base/galery.html', context)

def syarat_ketentuan(request):
    context = {

    }
    return render(request, 'base/sk.html', context)