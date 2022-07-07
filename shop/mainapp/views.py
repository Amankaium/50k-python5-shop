from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Product, Category, Parameter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator





def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'mainapp/home.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product(request):
    product = Product.objects.all()
    parameters = Parameter.objects.all()             
    return render(request,
                  'mainapp/product.html',
                  {'products': product,
                  'parameters': parameters})


                  

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
