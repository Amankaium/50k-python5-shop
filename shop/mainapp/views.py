from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def home(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'mainapp/home.html', data)

def product(request):
    
    return render(request, 'mainapp/product.html')

def base(request):
    products = Product.objects.all()

    data = {
        'products': products,
    }
    return render(request, 'mainapp/base.html', data)